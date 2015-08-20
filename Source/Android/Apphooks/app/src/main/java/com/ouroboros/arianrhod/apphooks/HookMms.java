package com.ouroboros.arianrhod.apphooks;

import android.app.Activity;
import android.util.TypedValue;
import android.view.View;
import android.view.ViewGroup.LayoutParams;
import android.view.Gravity;
import android.widget.Button;
import android.widget.LinearLayout;

import java.util.ArrayList;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;

public class HookMms implements IXposedHookLoadPackage {
    @Override
    public void handleLoadPackage(LoadPackageParam pkg) throws Throwable {
        XposedHelpers.findAndHookMethod("com.android.mms.quickmessage.QuickMessagePopup", pkg.classLoader, "setupViews", new XC_MethodHook() {
            @Override
            protected void afterHookedMethod(MethodHookParam param) throws Throwable {
                final Activity thiz = (Activity)param.thisObject;
                LinearLayout layout = (LinearLayout)thiz.findViewById(0x7F0F005A);

                final Button closeButton = (Button)XposedHelpers.getObjectField(thiz, "mCloseButton");
                final Button removeButton = new Button(thiz);

                removeButton.setText("刪除");
                removeButton.setTextSize(TypedValue.COMPLEX_UNIT_SP, 14.f);
                removeButton.setGravity(Gravity.CENTER);
                removeButton.setMinWidth(48);
                removeButton.setMaxLines(2);

                LayoutParams params = new LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);

                layout = (LinearLayout)layout.getChildAt(0);
                layout.addView(removeButton, 1, params);

                removeButton.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        int currentPage = XposedHelpers.getIntField(thiz, "mCurrentPage");
                        HookLoadPackage.log("currentPage = %d", currentPage);
                        ArrayList messageList = (ArrayList)XposedHelpers.getObjectField(thiz, "mMessageList");
                        Object quickMessage = messageList.get(XposedHelpers.getIntField(thiz, "mCurrentPage"));

                        closeButton.performClick();

//                        long threadid = (long)XposedHelpers.callMethod(quickMessage, "getThreadId");
//                        XposedHelpers.callMethod(thiz, "removeMatchingMessages", threadid);
                    }
                });
            }
        });
    }
}
