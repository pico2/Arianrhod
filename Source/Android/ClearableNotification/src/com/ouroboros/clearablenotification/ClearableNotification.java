package com.ouroboros.clearablenotification;

import java.io.ByteArrayOutputStream;
import java.lang.Integer;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Map;

import android.app.Notification;
import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;
import de.robv.android.xposed.XposedBridge;
import android.os.Looper;
import android.util.Log;

public class ClearableNotification implements IXposedHookLoadPackage {

    final protected static char[] hexArray = "0123456789ABCDEF".toCharArray();

    public static String bytesToHex(byte[] bytes) {
        char[] hexChars = new char[bytes.length * 2];
        for ( int j = 0; j < bytes.length; j++ ) {
            int v = bytes[j] & 0xFF;
            hexChars[j * 2] = hexArray[v >>> 4];
            hexChars[j * 2 + 1] = hexArray[v & 0x0F];
        }
        return new String(hexChars);
    }

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

    public String currentTime() {
        Date date=new Date();
        return new String(new SimpleDateFormat("yyyy.MM.dd HH:mm:ss").format(date));
    }

    public void log(Object obj) {
        log(String.format("%s", obj));
    }

    public void log(String text) {
        log("%s", String.format("%s", text));
    }

    public void log(String format, Object... args) {
        XposedBridge.log(String.format("[%s][%d] %s", currentTime(), Thread.currentThread().getId(), String.format(format, args)));
    }

    public void log(Throwable e) {
        log("%s", Log.getStackTraceString(e));
    }

    public void mm_log(String format, Object[] objs) {
        log(String.format(format, objs));
    }

    Class<?> AudioEncodHelper = null;
    // Class<?> SlightEncodeH = null;
    // Class<?> PByteArray = null;
    // Class<?> ClientRequestPacket = null;
    // Class<?> MMProtocalJni = null;

    boolean packHooked = false;

    public class ClientRequest {

        Object encoder;

        public ClientRequest(Object encoder) {
            this.encoder = encoder;
        }

        public byte[] getBuffer() {
            return (byte[])XposedHelpers.getObjectField(this.encoder, "eKO");
        }

        public ClientRequestPacketWrap getPacket() {
            return new ClientRequestPacketWrap(XposedHelpers.getObjectField(this.encoder, "eJQ"));
        }
    }

    public class ClientRequestPacketWrap {
        Object packet;

        ClientRequestPacketWrap(Object packet) {
            this.packet = packet;
        }

        public byte[] toBinary() {
            return (byte[])XposedHelpers.callMethod(this.packet, "Dh");
        }
    }

    private void initClasses(LoadPackageParam pkg) {

        // this.SlightEncodeH = XposedHelpers.findClass("com.tencent.mm.plugin.sight.encode.a.h", pkg.classLoader);
        //log(this.SlightEncodeH.toString());

        this.AudioEncodHelper = XposedHelpers.findClass("com.tencent.mm.plugin.sight.encode.a.e", pkg.classLoader);
        //log(this.AudioEncodHelper.toString());

        // this.PByteArray = XposedHelpers.findClass("com.tencent.mm.pointers.PByteArray", pkg.classLoader);
//        log(this.PByteArray);

        // this.ClientRequestPacket = XposedHelpers.findClass("com.tencent.mm.protocal.i.c", pkg.classLoader);
//        log(this.ClientRequest);

        // this.MMProtocalJni = XposedHelpers.findClass("com.tencent.mm.protocal.MMProtocalJni", pkg.classLoader);
//        log(this.MMProtocalJni);
    }

    private void hookWeChat(final LoadPackageParam pkg) {

//        XposedHelpers.findAndHookMethod("java.lang.System", pkg.classLoader, "load", String.class, new XC_MethodHook() {
//            @Override
//            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
//                log(param.args[0]);
//            }
//        });

        initClasses(pkg);

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
             XposedHelpers.setObjectField(XposedHelpers.getObjectField(param.thisObject, "fjq"), "fjj", 0);
         }
     });

       // "ERROR record duration, %dms !!!"

       XposedHelpers.findAndHookMethod("com.tencent.mm.plugin.sight.encode.ui.bi", pkg.classLoader, "lO", new XC_MethodHook() {
           @Override
           protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
               XposedHelpers.callMethod(XposedHelpers.getObjectField(param.thisObject, "fnu"), "s", 0.f);
               param.setResult(true);
               //log("updateProgress");
               //log(new Exception());
               //log(Boolean.toString(Looper.getMainLooper().getThread() == Thread.currentThread()));
           }
       });

        // mm hit MM_DATA_SYSCMD_NEWXML_SUBTYPE_REVOKE

        XposedHelpers.findAndHookMethod("com.tencent.mm.sdk.platformtools.p", pkg.classLoader, "z", String.class, String.class, String.class, new XC_MethodHook() {
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
