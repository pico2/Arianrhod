package com.ouroboros.arianrhod.apphooks;

import java.util.Map;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import java.lang.reflect.Constructor;

class StepCounterListener implements SensorEventListener {
    private SensorEventListener mListener;

    public StepCounterListener(SensorEventListener listener) {
        mListener = listener;
    }

    public void onAccuracyChanged(Sensor sensor, int accuracy) {
        mListener.onAccuracyChanged(sensor, accuracy);
    }

    public void onSensorChanged(SensorEvent event) {
        HookLoadPackage.log("step %f", event.values[0]);
        event.values[0] = event.values[0] * 100.f;
        HookLoadPackage.log("step 2 %f", event.values[0]);
        mListener.onSensorChanged(event);
    }
}

public class HookMobileQQ implements IXposedHookLoadPackage {
    @Override
    public void handleLoadPackage(final LoadPackageParam pkg) throws Throwable {
        XposedHelpers.findAndHookMethod("android.hardware.SensorManager", pkg.classLoader, "registerListener", SensorEventListener.class, Sensor.class, Integer.TYPE, Integer.TYPE, new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(final MethodHookParam param) throws Throwable {
                final SensorEventListener listener = (SensorEventListener)param.args[0];
                final Sensor sensor = (Sensor)param.args[1];
                final int interval = (int)param.args[3] / 1000;
                if (sensor.getType() == Sensor.TYPE_STEP_COUNTER) {
                    Constructor<SensorEvent> constructor = SensorEvent.class.getDeclaredConstructor(int.class);
                    constructor.setAccessible(true);
                    SensorEvent sensorEvent = constructor.newInstance(1);
                    sensorEvent.values[0] = 100 * 10000.f;
                    listener.onSensorChanged(sensorEvent);

//                    param.args[0] = new StepCounterListener(listener);
//                    param.args[3] = 1800 * 1000 * 1000;

//                    new Thread() {
//                        @Override
//                        public void run() {
//                            float step = 100.f;
//                            while (true) {
//                                try {
//                                    Constructor<SensorEvent> constructor = SensorEvent.class.getDeclaredConstructor(int.class);
//                                    constructor.setAccessible(true);
//                                    SensorEvent sensorEvent = constructor.newInstance(1);
//                                    sensorEvent.values[0] = step;
//                                    HookLoadPackage.log("step: %f", step);
//                                    listener.onSensorChanged(sensorEvent);
//                                    step += 1000.f;
//
//                                    if (step > 30000.f) {
//                                        step = 1.f;
//                                    }
//
//                                    Thread.sleep(1000);
//                                } catch (java.lang.Exception e) {
//                                    HookLoadPackage.log(e);
//                                }
//                            }
//                        }
//                    }.start();
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
}
