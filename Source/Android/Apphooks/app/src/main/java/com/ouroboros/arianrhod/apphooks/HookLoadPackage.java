package com.ouroboros.arianrhod.apphooks;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;

import android.util.Log;

import de.robv.android.xposed.XposedBridge;
import java.text.SimpleDateFormat;
import java.util.Date;

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
        switch (pkg.packageName) {
            case "pl.solidexplorer2":
                new HookSolidExplorer().handleLoadPackage(pkg);
                break;

            case "com.tencent.mm":
                new HookWeChat().handleLoadPackage(pkg);
                break;

            case "flar2.exkernelmanager":
                new HookExkernelManager().handleLoadPackage(pkg);
                break;
        }
    }
}
