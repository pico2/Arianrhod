package com.ouroboros.arianrhod.apphooks;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;

public class HookExkernelManager implements IXposedHookLoadPackage {
    @Override
    public void handleLoadPackage(LoadPackageParam pkg) throws Throwable {
        XposedHelpers.findAndHookMethod("flar2.exkernelmanager.utilities.k", pkg.classLoader, "a", new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                param.setResult(true);
            }
        });
    }
}
