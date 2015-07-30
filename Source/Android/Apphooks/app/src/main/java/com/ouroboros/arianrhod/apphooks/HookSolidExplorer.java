package com.ouroboros.arianrhod.apphooks;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;

public class HookSolidExplorer implements IXposedHookLoadPackage {
    @Override
    public void handleLoadPackage(LoadPackageParam pkg) throws Throwable {
        final Class<?> SELicenseManager$AppLicenseCallback = XposedHelpers.findClass("pl.solidexplorer.SELicenseManager$AppLicenseCallback", pkg.classLoader);
        final Class<?> PreferenceObfuscator = XposedHelpers.findClass("com.google.android.vending.licensing.PreferenceObfuscator", pkg.classLoader);
        final Class<?> Preference = XposedHelpers.findClass("pl.solidexplorer.preferences.Preferences", pkg.classLoader);

//        XposedHelpers.findAndHookMethod("pl.solidexplorer.SELicenseManager", pkg.classLoader, "checkTrial", SELicenseManager$AppLicenseCallback, PreferenceObfuscator, new XC_MethodHook() {
//            @Override
//            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
//                Object cb = param.args[0];
//
//                XposedHelpers.callMethod(cb, "allowAccess", true);
//                XposedHelpers.callStaticMethod(Preference, "put", "trial_left", 1209600000, false);
//                param.setResult(null);
//            }
//        });

        XposedHelpers.findAndHookMethod("pl.solidexplorer.SELicenseManager", pkg.classLoader, "checkUnlockerLicense", SELicenseManager$AppLicenseCallback, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                Object cb = param.args[0];

                XposedHelpers.callStaticMethod(Preference, "put", "license_status", "LEGACY LICENSE", false);
                XposedHelpers.callMethod(cb, "allowAccess", true);
                param.setResult(true);
            }
        });
    }
}
