package com.ouroboros.arianrhod.apphooks;

import java.util.Map;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;

public class HookWeChat implements IXposedHookLoadPackage {
    @Override
    public void handleLoadPackage(LoadPackageParam pkg) throws Throwable {

//        XposedHelpers.findAndHookMethod("java.lang.System", pkg.classLoader, "load", String.class, new XC_MethodHook() {
//            @Override
//            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
//                log(param.args[0]);
//            }
//        });

//        initClasses(pkg);

//        for (String method : new String[] {"c", "d", "e", "f", "g", "i", "v", "w"})
//        {
//            XposedHelpers.findAndHookMethod("com.tencent.mm.sdk.platformtools.r", pkg.classLoader, method, String.class, String.class, Object[].class, hook);
//        }

        // "error pcm duration %d"

//        XposedHelpers.findAndHookMethod("com.tencent.mm.plugin.sight.encode.a.e", pkg.classLoader, "g", AudioEncodHelper, new XC_MethodHook() {
//           @Override
//           protected void afterHookedMethod(MethodHookParam param) throws Throwable {
//
//               //I/Xposed  ( 7423):      at beforeHookedMethod
//               //I/Xposed  ( 7423):      at handleHookedMethod
//               //I/Xposed  ( 7423):      at g
//               //I/Xposed  ( 7423):      at c
//
//               Exception e = new Exception();
//               StackTraceElement[] elements = e.getStackTrace();
//
//               // log(elements[3].getClassName());
//               // log(elements[3].getMethodName());
//
//               if (elements[3].getClassName().equals("com.tencent.mm.plugin.sight.encode.a.h") == false) {
//                   return;
//               }
//
//               if (elements[3].getMethodName().equals("c") == false) {
//                   return;
//               }
//
//               param.setResult(0);
//           }
//       });


        XposedHelpers.findAndHookMethod("com.tencent.mm.plugin.sight.encode.a.h", pkg.classLoader, "d", byte[].class, int.class, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                XposedHelpers.setObjectField(XposedHelpers.getObjectField(param.thisObject, "fqA"), "fqt", 0);
            }
        });

        // "ERROR record duration, %dms !!!"

        XposedHelpers.findAndHookMethod("com.tencent.mm.plugin.sight.encode.ui.bi", pkg.classLoader, "lQ", new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                XposedHelpers.callMethod(XposedHelpers.getObjectField(param.thisObject, "fuE"), "w", 0.f);
                param.setResult(true);
                //log("updateProgress");
                //log(new Exception());
                //log(Boolean.toString(Looper.getMainLooper().getThread() == Thread.currentThread()));
            }
        });

        // mm hit MM_DATA_SYSCMD_NEWXML_SUBTYPE_REVOKE

        XposedHelpers.findAndHookMethod("com.tencent.mm.sdk.platformtools.q", pkg.classLoader, "A", String.class, String.class, String.class, new XC_MethodHook() {
            @Override
            protected void afterHookedMethod(MethodHookParam param) throws Throwable {
//                log("what the fuck");

                if (param.hasThrowable() || param.getResult() == null)
                    return;

                @SuppressWarnings("unchecked")
                Map<String, String> result = (Map<String, String>)param.getResult();

                String type = result.get(".sysmsg.$type");

//               log("type = " + type);

                if (type != null && type.equals("revokemsg"))
                    result.put(".sysmsg.$type",  "disabled_" + type);
            }
        });
    }
}
