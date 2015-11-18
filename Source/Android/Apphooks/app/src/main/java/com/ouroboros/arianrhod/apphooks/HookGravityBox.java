package com.ouroboros.arianrhod.apphooks;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;
import android.content.Context;
import android.os.Bundle;

public class HookGravityBox implements IXposedHookLoadPackage {
    @Override
    public void handleLoadPackage(LoadPackageParam pkg) throws Throwable {
        XposedHelpers.findAndHookMethod("com.ceco.marshmallow.gravitybox.UnlockActivity", pkg.classLoader, "checkPolicyOk", Context.class, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
//                HookLoadPackage.log("hook in");
                param.setResult(true);
            }
        });

        XposedHelpers.findAndHookConstructor("com.ceco.marshmallow.gravitybox.GravityBoxSettings$SystemProperties", pkg.classLoader, Bundle.class, new XC_MethodHook() {
            @Override
            protected void afterHookedMethod(MethodHookParam param) throws Throwable {
//                HookLoadPackage.log("hook in 2");
                XposedHelpers.setBooleanField(param.thisObject, "uuidRegistered", true);
            }
        });
    }
}
