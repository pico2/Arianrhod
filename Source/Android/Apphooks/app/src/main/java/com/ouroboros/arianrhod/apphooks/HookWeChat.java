package com.ouroboros.arianrhod.apphooks;

import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Matrix;
import android.graphics.Paint;
import android.graphics.Point;
import android.graphics.Rect;
import android.graphics.RectF;
import android.os.Handler;
import android.util.AttributeSet;
import android.widget.ImageView;

import java.util.Map;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.XC_MethodReplacement;
import java.lang.reflect.Method;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;

class WeChatWakerLock {
    public WeChatWakerLock(Context arg7) {
    }

    protected void finalize() {
    }

    private String getCallerStack() {
        return "<native>";
    }

    public String getCreatePosStackLine() {
        return "";
    }

    public int innerWakeLockHashCode() {
        return 0;
    }

    public boolean isLocking() {
        return false;
    }

    public void lock() {
    }

    public void lock(String arg8) {
    }

    public void lock(long arg2) {
    }

    public void lock(long arg8, String arg10) {
    }

    public void unLock() {
    }
}

public class HookWeChat implements IXposedHookLoadPackage {
    @Override
    public void handleLoadPackage(LoadPackageParam pkg) throws Throwable {
        hookWakerLock(pkg);

        // "error pcm duration %d"

        XposedHelpers.findAndHookMethod("com.tencent.mm.plugin.sight.encode.a.d$3", pkg.classLoader, "d", byte[].class, int.class, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                XposedHelpers.setObjectField(XposedHelpers.getObjectField(param.thisObject, "hkX"), "hkQ", 0);
            }
        });

        // "ERROR record duration, %dms !!!"

        XposedHelpers.findAndHookMethod("com.tencent.mm.plugin.sight.encode.ui.SightCameraView$1", pkg.classLoader, "lO", new XC_MethodReplacement() {
            @Override
            protected Boolean replaceHookedMethod(MethodHookParam param) throws Throwable {
                Object obj1 = XposedHelpers.getObjectField(param.thisObject, "hoV");
                Object obj2 = XposedHelpers.getObjectField(obj1, "hoI");

                float v2 = ((Long)XposedHelpers.callMethod(obj2, "aBz")).floatValue() / 6500.f;
                if (Float.compare(v2, 0.f) > 0) {
                    if (Float.compare(v2, 1f) <= 0) {
                        XposedHelpers.callMethod(obj1, "K", v2);
                    } else {
                        XposedHelpers.callMethod(obj1, "K", 1f);
                    }
                }

                return true;
            }
        });

        // mm hit MM_DATA_SYSCMD_NEWXML_SUBTYPE_REVOKE

        XposedHelpers.findAndHookMethod("com.tencent.mm.sdk.platformtools.bf", pkg.classLoader, "p", String.class, String.class, new XC_MethodHook() {
            @Override
            protected void afterHookedMethod(MethodHookParam param) throws Throwable {
//            HookLoadPackage.log("what the fuck");

            if (param.hasThrowable() || param.getResult() == null)
                return;

            @SuppressWarnings("unchecked")
            Map<String, String> result = (Map<String, String>)param.getResult();

            String type = result.get(".sysmsg.$type");

//           log("type = " + type);

            if (type != null && type.equals("revokemsg"))
                result.put(".sysmsg.$type",  "disabled_" + type);
            }
        });

        // scheduleHideClip, alphaChangeStep: %s
        // snsblurs_
        // snsblurt_

//        XposedHelpers.findAndHookMethod("com.tencent.mm.plugin.sns.lucky.ui.LuckyRevealImageView", pkg.classLoader, "onDraw", Canvas.class, new XC_MethodHook() {
//            @Override
//            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
//                Canvas canvas = (Canvas)param.args[0];
//                Bitmap bitmap = (Bitmap)XposedHelpers.getObjectField(param.thisObject, "gIW");
//                Paint paint = (Paint)XposedHelpers.getObjectField(param.thisObject, "cIZ");
//
//                if (bitmap != null) {
//                    Point screenSize = (Point)XposedHelpers.callMethod(param.thisObject, "getScreenSize");
//                    int width, height;
//
//                    width = bitmap.getWidth();
//                    height = bitmap.getHeight();
//
//                    Matrix m = new Matrix();
//                    m.setRectToRect(new RectF(0, 0, width, height), new RectF(0, 0, screenSize.x, screenSize.y), Matrix.ScaleToFit.CENTER);
//                    bitmap = Bitmap.createBitmap(bitmap, 0, 0, width, height, m, true);
//
//                    canvas.save();
//                    width = bitmap.getWidth();
//                    height = bitmap.getHeight();
//                    canvas.drawBitmap(bitmap, null, new Rect(0, 0, width, height), paint);
//                    canvas.restore();
//                }
//
//                param.setResult(null);
//            }
//        });
    }

    private void hookWakerLock(LoadPackageParam pkg) {
//        Class<?> WakerLock = XposedHelpers.findClass("com.tencent.mm.jni.platformcomm.WakerLock", pkg);
//        Class<?> WakeLock = XposedHelpers.findClass("android.os.PowerManager.WakeLock", pkg.classLoader);

        XposedHelpers.findAndHookMethod("android.os.PowerManager", pkg.classLoader, "newWakeLock", int.class, String.class, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                String tag = (String)param.args[1];
                if (tag.startsWith("WakerLock:")) {
                    param.args[1] = "WakerLock:WeChat";
                }
            }
        });

        if (true) return;

//        XC_MethodHook nop = new XC_MethodHook() {
//            @Override
//            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
//                param.setResult(null);
//            }
//        };

//        XposedHelpers.findAndHookMethod(WakeLock, "acquire", nop);
//        XposedHelpers.findAndHookMethod(WakeLock, "acquire", long.class, nop);
//        XposedHelpers.findAndHookMethod(WakeLock, "release", nop);
//        XposedHelpers.findAndHookMethod(WakeLock, "release", int.class, nop);

//        XposedHelpers.findAndHookMethod("com.tencent.mm.jni.platformcomm.Alarm", pkg.classLoader, "a", long.class, int.class, Context.class, new XC_MethodHook() {
//            @Override
//            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
//                HookLoadPackage.log("fuck alarm");
//                param.setResult(true);
//            }
//        });

        XposedHelpers.findAndHookMethod("android.content.ContextWrapper", pkg.classLoader, "registerReceiver", BroadcastReceiver.class, IntentFilter.class, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                IntentFilter filter = (IntentFilter)param.args[1];
                String action = filter.getAction(0);

                if (action.startsWith("ALARM_ACTION(") && action.endsWith(")")) {
                    HookLoadPackage.log("fuck alarm 1 %s", action);
                    param.setResult(null);
                }
            }
        });

        XposedHelpers.findAndHookMethod("android.app.AlarmManager", pkg.classLoader, "set", int.class, long.class, PendingIntent.class, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                PendingIntent pendingIntent = (PendingIntent)param.args[2];

                Method getIntent = PendingIntent.class.getDeclaredMethod("getIntent");
                Intent intent = (Intent)getIntent.invoke(pendingIntent);
                String action = intent.getAction();

                if (action.startsWith("ALARM_ACTION(") && action.endsWith(")")) {
                    HookLoadPackage.log("fuck alarm 2 %s", action);
                    param.setResult(null);
                }
            }
        });

        XposedHelpers.findAndHookMethod("android.content.ContextWrapper", pkg.classLoader, "registerReceiver", BroadcastReceiver.class, IntentFilter.class, String.class, Handler.class, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                IntentFilter filter = (IntentFilter)param.args[1];
                String action = filter.getAction(0);

                if (action.startsWith("ALARM_ACTION(") && action.endsWith(")")) {
                    HookLoadPackage.log("fuck alarm 3 %s", action);
                    param.setResult(null);
                }
            }
        });
    }
}
