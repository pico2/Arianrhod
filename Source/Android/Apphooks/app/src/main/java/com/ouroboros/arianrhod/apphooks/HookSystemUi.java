package com.ouroboros.arianrhod.apphooks;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;
import android.widget.TextView;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class HookSystemUi implements IXposedHookLoadPackage {
    @Override
    public void handleLoadPackage(LoadPackageParam pkg) throws Throwable {
        XposedHelpers.findAndHookMethod("com.android.systemui.statusbar.policy.Clock", pkg.classLoader, "updateClock", new XC_MethodHook() {
            @Override
            protected void afterHookedMethod(MethodHookParam param) throws Throwable {
                TextView clockView = (TextView)XposedHelpers.getObjectField(param.thisObject, "mClockView");
                String time = clockView.getText().toString();

                time = new SimpleDateFormat("E MM.dd", Locale.getDefault()).format(new Date()) + " " + time;
                clockView.setText(time);
            }
        });
    }
}
