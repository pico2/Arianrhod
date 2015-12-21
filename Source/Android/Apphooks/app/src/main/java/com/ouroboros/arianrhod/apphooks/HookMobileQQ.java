package com.ouroboros.arianrhod.apphooks;

import java.util.Map;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorManager;
import android.hardware.SensorEventListener;
import java.lang.reflect.Constructor;

public class HookMobileQQ implements IXposedHookLoadPackage {
    @Override
    public void handleLoadPackage(final LoadPackageParam pkg) throws Throwable {
        XposedHelpers.findAndHookMethod("android.hardware.SensorManager", pkg.classLoader, "registerListener", SensorEventListener.class, Sensor.class, Integer.TYPE, Integer.TYPE, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(final MethodHookParam param) throws Throwable {
                final SensorManager sensorManager = (SensorManager)param.thisObject;
                final SensorEventListener listener = (SensorEventListener)param.args[0];
                final Sensor sensor = (Sensor)param.args[1];
                final int interval = (int)param.args[3] / 1000;

                if (sensor.getType() == Sensor.TYPE_STEP_COUNTER) {
//                    Constructor<SensorEvent> constructor = SensorEvent.class.getDeclaredConstructor(int.class);
//                    constructor.setAccessible(true);
//                    SensorEvent sensorEvent = constructor.newInstance(1);
//                    sensorEvent.values[0] = 100 * 10000.f;
//                    listener.onSensorChanged(sensorEvent);

                    param.args[0] = new StepCounterListener(sensorManager, listener);
//                    param.args[3] = 1800 * 1000 * 1000;

//                    thread(param);
//                    param.setResult(true);
                }
            }
        });

//        XposedHelpers.findAndHookMethod("android.hardware.SensorManager", pkg.classLoader, "getDefaultSensor", int.class, new XC_MethodHook() {
//            @Override
//            protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
//                if ((int)param.args[0] == Sensor.TYPE_STEP_COUNTER) {
//                    param.setResult(null);
//                }
//            }
//        });
    }

    private void thread(final XC_MethodHook.MethodHookParam param) {
        final SensorEventListener listener = (SensorEventListener)param.args[0];
        final Sensor sensor = (Sensor)param.args[1];
        final int interval = (int)param.args[3] / 1000;
        new Thread() {
            @Override
            public void run() {
                float step = 30000.f;
                while (true) {
                    try {
                        Constructor<SensorEvent> constructor = SensorEvent.class.getDeclaredConstructor(int.class);
                        constructor.setAccessible(true);
                        SensorEvent sensorEvent = constructor.newInstance(1);

                        for (int i = 0; i != 20; i++) {
                            sensorEvent.values[0] = step++;
                            HookLoadPackage.log("step: %f", sensorEvent.values[0]);
                            listener.onSensorChanged(sensorEvent);
                        }

                        Thread.sleep(10000);
                    } catch (java.lang.Exception e) {
                        HookLoadPackage.log(e);
                        break;
                    }
                }
            }
        }.start();
    }
}
