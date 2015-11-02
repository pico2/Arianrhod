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


        XposedHelpers.findAndHookMethod("com.tencent.mm.plugin.sight.encode.a.d$3", pkg.classLoader, "d", byte[].class, int.class, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                XposedHelpers.setObjectField(XposedHelpers.getObjectField(param.thisObject, "fPp"), "fPi", 0);
            }
        });

        // "ERROR record duration, %dms !!!"

        XposedHelpers.findAndHookMethod("com.tencent.mm.plugin.sight.encode.ui.SightCameraView$1", pkg.classLoader, "lV", new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                Object obj1 = XposedHelpers.getObjectField(param.thisObject, "fTr");
                Object obj2 = XposedHelpers.getObjectField(obj1, "fTf");

                float v2 = ((Long)XposedHelpers.callMethod(obj2, "aqj")).floatValue() / 6500.f;
                if (Float.compare(v2, 0.f) > 0) {
                    if (Float.compare(v2, 1f) <= 0) {
                        XposedHelpers.callMethod(obj1, "z", v2);
                    } else {
                        XposedHelpers.callMethod(obj1, "z", 1f);
                    }
                }

                param.setResult(true);
            }
        });

        // mm hit MM_DATA_SYSCMD_NEWXML_SUBTYPE_REVOKE

        XposedHelpers.findAndHookMethod("com.tencent.mm.sdk.platformtools.q", pkg.classLoader, "C", String.class, String.class, String.class, new XC_MethodHook() {
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
