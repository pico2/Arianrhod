package com.ouroboros.clearablenotification;

import java.lang.Integer;
import android.app.Notification;
import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;
import de.robv.android.xposed.XposedBridge;
import android.os.Looper;
import android.util.Log;

public class ClearableNotification implements IXposedHookLoadPackage {

    @Override
    public void handleLoadPackage(LoadPackageParam pkg) throws Throwable {

        if (pkg.packageName.equals("com.tencent.mm")) {
            hookWeChat(pkg);
        }

        if (true)
            return;

        if (pkg.packageName.equals("com.tencent.mobileqq") == false)
            return;

        XposedHelpers.findAndHookMethod("android.app.NotificationManager", pkg.classLoader, "notify", int.class, Notification.class, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                modifyFlag(param.args[1]);
                super.beforeHookedMethod(param);
            }
        });

        XposedHelpers.findAndHookMethod("android.app.NotificationManager", pkg.classLoader, "notify", String.class, int.class, Notification.class, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                modifyFlag(param.args[2]);
                super.beforeHookedMethod(param);
            }
        });
    }

    public void modifyFlag(Object obj){
        Notification notify = (Notification) obj;
        notify.flags &= ~Notification.FLAG_ONGOING_EVENT;
        notify.flags |= Notification.FLAG_AUTO_CANCEL;
    }

    public void log(Object obj) {
        XposedBridge.log(obj.toString());
    }

    public void log(String text) {
        XposedBridge.log(text);
    }

    public void log(Throwable e) {
        e.getStackTrace();
        XposedBridge.log(Log.getStackTraceString(e));
    }

    public void mm_log(String format, Object[] objs) {
        log(String.format(format, objs));
    }

    Class<?> SlightEncodeH = null;
    Class<?> AudioEncodHelper = null;

    private void hookWeChat(LoadPackageParam pkg) {

        this.SlightEncodeH = XposedHelpers.findClass("com.tencent.mm.plugin.sight.encode.a.h", pkg.classLoader);
        //log(this.SlightEncodeH.toString());

        this.AudioEncodHelper = XposedHelpers.findClass("com.tencent.mm.plugin.sight.encode.a.d", pkg.classLoader);
        //log(this.AudioEncodHelper.toString());

//        XposedHelpers.findAndHookMethod("com.tencent.mm.sdk.platformtools.r", pkg.classLoader, "i", String.class, String.class, Object[].class, new XC_MethodHook() {
//            @Override
//            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
//                mm_log((String)param.args[1], (Object[])param.args[2]);
//            }
//        });
//
//        XposedHelpers.findAndHookMethod("com.tencent.mm.sdk.platformtools.r", pkg.classLoader, "w", String.class, String.class, Object[].class, new XC_MethodHook() {
//            @Override
//            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
//                mm_log((String)param.args[1], (Object[])param.args[2]);
//            }
//        });

        // "error pcm duration %d"

        XposedHelpers.findAndHookMethod("com.tencent.mm.plugin.sight.encode.a.d", pkg.classLoader, "g", AudioEncodHelper, new XC_MethodHook() {
            @Override
            protected void afterHookedMethod(MethodHookParam param) throws Throwable {

                //I/Xposed  ( 7423):      at beforeHookedMethod
                //I/Xposed  ( 7423):      at handleHookedMethod
                //I/Xposed  ( 7423):      at g
                //I/Xposed  ( 7423):      at c

                Exception e = new Exception();
                StackTraceElement[] elements = e.getStackTrace();

                //log(elements[3].getClassName());
                //log(elements[3].getMethodName());

                if (elements[3].getClassName().equals("com.tencent.mm.plugin.sight.encode.a.g") == false) {
                    return;
                }

                if (elements[3].getMethodName().equals("c") == false) {
                    return;
                }

                param.setResult(0);
            }
        });

        // "ERROR record duration, %dms !!!"

        XposedHelpers.findAndHookMethod("com.tencent.mm.plugin.sight.encode.ui.as", pkg.classLoader, "rC", new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                XposedHelpers.callMethod(XposedHelpers.getObjectField(param.thisObject, "iuv"), "C", 0.f);
                param.setResult(true);
                //log("updateProgress");
                //log(new Exception());
                //log(Boolean.toString(Looper.getMainLooper().getThread() == Thread.currentThread()));
            }
        });
    }
}
