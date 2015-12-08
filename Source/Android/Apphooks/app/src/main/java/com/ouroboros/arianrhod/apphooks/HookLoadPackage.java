package com.ouroboros.arianrhod.apphooks;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;

import android.util.Log;
import android.hardware.Sensor;

import de.robv.android.xposed.XposedBridge;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Date;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

public class HookLoadPackage implements IXposedHookLoadPackage {
    public static String currentTime() {
        Date date=new Date();
        return new String(new SimpleDateFormat("yyyy.MM.dd HH:mm:ss").format(date));
    }

    public static void log(Object obj) {
        log(String.format("%s", obj));
    }

    public static void log(String text) {
        log("%s", String.format("%s", text));
    }

    public static void log(String format, Object... args) {
        XposedBridge.log(String.format("[%s][%d] %s", currentTime(), Thread.currentThread().getId(), String.format(format, args)));
    }

    public static void log(Throwable e) {
        log("%s", Log.getStackTraceString(e));
    }

    @Override
    public void handleLoadPackage(final LoadPackageParam pkg) throws Throwable {
        removeStupidSensors(pkg);

        switch (pkg.packageName) {
            case "pl.solidexplorer2":
//                new HookSolidExplorer().handleLoadPackage(pkg);
                break;

            case "com.tencent.mm":
                new HookWeChat().handleLoadPackage(pkg);
                break;

            case "com.tencent.mobileqq":
//                new HookMobileQQ().handleLoadPackage(pkg);
                break;

            case "flar2.exkernelmanager":
//                new HookExkernelManager().handleLoadPackage(pkg);
                break;

            case "com.ceco.marshmallow.gravitybox":
                new HookGravityBox().handleLoadPackage(pkg);
                break;

            case "com.android.systemui":
//                new HookSystemUi().handleLoadPackage(pkg);
                break;

            case "com.android.mms":
//                new HookMms().handleLoadPackage(pkg);
                break;
        }
    }

    private static final Set<Integer> SENSORS = new HashSet<>(Arrays.asList(
        new Integer[]{
            Sensor.TYPE_STEP_COUNTER,
            Sensor.TYPE_STEP_DETECTOR,
        }
    ));

    void removeStupidSensors(LoadPackageParam lpparam) {
        XposedHelpers.findAndHookMethod("android.hardware.SystemSensorManager", lpparam.classLoader, "getFullSensorList", new XC_MethodHook() {
            @Override
            protected void afterHookedMethod(MethodHookParam param) throws Throwable {
                List<Sensor> fullSensorList = (List<Sensor>) param.getResult();
                Iterator<Sensor> iterator = fullSensorList.iterator();
                while (iterator.hasNext()) {
                    Sensor sensor = iterator.next();
                    if (SENSORS.contains(sensor.getType())) {
                        iterator.remove();
                    }
                }
                param.setResult(fullSensorList);
            }
        });
    }
}
