package com.ouroboros.arianrhod.apphooks;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;
import com.ouroboros.arianrhod.apphooks.HookWeChat;

public class HookLoadPackage implements IXposedHookLoadPackage {
    @Override
    public void handleLoadPackage(LoadPackageParam pkg) throws Throwable {
        if (pkg.packageName.equals("com.tencent.mm")) {
            new HookWeChat().handleLoadPackage(pkg);
            return;
        }
    }
}
