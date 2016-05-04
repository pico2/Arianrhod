package com.ouroboros.arianrhod.apphooks;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;

import android.app.Activity;
import android.content.Context;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
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


class StepCounterListener implements SensorEventListener {
    private SensorManager mSensorManager;
    private SensorEventListener mListener;
    private int mCount;

    public StepCounterListener(SensorManager sensorManager, SensorEventListener listener) {
        mSensorManager = sensorManager;
        mListener = listener;
        mCount = 0;
    }

    public void onAccuracyChanged(Sensor sensor, int accuracy) {
        mListener.onAccuracyChanged(sensor, accuracy);
    }

    public void onSensorChanged(SensorEvent event) {
        event.values[0] = 40000.f + event.values[0];
        HookLoadPackage.log("step 2 %f", event.values[0]);
        mListener.onSensorChanged(event);
    }
}

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
//            case "pl.solidexplorer2":
//                new HookSolidExplorer().handleLoadPackage(pkg);
//                break;

            case "com.tencent.mm":
                new HookWeChat().handleLoadPackage(pkg);
//                fakeStepCounter(pkg);
                break;

//            case "com.tencent.mobileqq":
//                fakeStepCounter(pkg);
//                new HookMobileQQ().handleLoadPackage(pkg);
//                break;

//            case "flar2.exkernelmanager":
//                new HookExkernelManager().handleLoadPackage(pkg);
//                break;

            case "com.ceco.marshmallow.gravitybox":
                new HookGravityBox().handleLoadPackage(pkg);
                break;

//            case "com.android.systemui":
//                new HookSystemUi().handleLoadPackage(pkg);
//                break;

//            case "com.android.mms":
//                new HookMms().handleLoadPackage(pkg);
//                break;

//            case "eu.chainfire.lumen":
//                XposedHelpers.findAndHookMethod("android.app.ApplicationPackageManager", pkg.classLoader, "getPackageInfo", String.class, int.class, new XC_MethodHook() {
//                    @Override
//                    protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
//                        String packageName = (String)param.args[0];
//                        if (packageName.equals("eu.chainfire.lumen.pro")) {
//                            param.args[0] = "com.android.systemui";
//                        }
//                    }
//                });
//                break;
        }
    }

    private void fakeStepCounter(final LoadPackageParam pkg) {
        XposedHelpers.findAndHookMethod("android.hardware.SensorManager", pkg.classLoader, "registerListener", SensorEventListener.class, Sensor.class, Integer.TYPE, Integer.TYPE, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(final MethodHookParam param) throws Throwable {
                final SensorManager sensorManager = (SensorManager)param.thisObject;
                final SensorEventListener listener = (SensorEventListener)param.args[0];
                final Sensor sensor = (Sensor)param.args[1];
                final int interval = (int)param.args[3] / 1000;

                if (sensor.getType() == Sensor.TYPE_STEP_COUNTER) {
                    param.args[0] = new StepCounterListener(sensorManager, listener);
                }
            }
        });
    }

    private static final Set<Integer> SENSORS = new HashSet<>(Arrays.asList(
        new Integer[]{
            Sensor.TYPE_STEP_COUNTER,
            Sensor.TYPE_STEP_DETECTOR,
        }
    ));

    void removeStupidSensors(LoadPackageParam pkg) {
        XposedHelpers.findAndHookMethod("android.hardware.SystemSensorManager", pkg.classLoader, "getFullSensorList", new XC_MethodHook() {
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
