package com.test.motionevent;

import java.text.SimpleDateFormat;
import java.util.Date;

import android.app.Activity;
import android.content.ContentValues;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.widget.EditText;

import com.example.traffic_light_map_show.dao.PersonDao;
import com.example.traffic_light_map_show.dao.PersonDaoImpl1;

public class MotionEventActivity extends Activity {
	private static final String TAG = "MotionEvent";
	String xyPosition=null;
	PersonDao pd1;
	PersonDao pd2;
	private SensorManager sensorManager = null;
	private Sensor sensor = null;
	private float gravity[] = new float[3];
	//����������Ҫ�õ���UIԪ��
		private EditText edtmsgcontent;
		private String ip="192.168.1.102";
		private int port=1818;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(new MotionView(this));
        pd1=new PersonDaoImpl1(getApplicationContext());
        pd2=new PersonDaoImpl1(getApplicationContext());
    	sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
		sensor = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
    }
    
    public class MotionView extends View {
    	private Paint mPaint = new Paint();
    	private int mAction;
    	private float mX;
    	private float mY;
    	public MotionView(Context c) {
    		super(c);
    		mAction = MotionEvent.ACTION_UP;
    		mX = 0;
    		mY = 0;
    	}
    	@Override
    	protected void onDraw(Canvas canvas) {
    		Paint paint = mPaint;
    		canvas.drawColor(Color.WHITE);
    		if(MotionEvent.ACTION_MOVE == mAction) {
    			paint.setColor(Color.RED);
    		}else if(MotionEvent.ACTION_UP == mAction) {
				paint.setColor(Color.GREEN);
			}else if(MotionEvent.ACTION_DOWN == mAction) {
				paint.setColor(Color.BLUE);
			}
    		canvas.drawCircle(mX, mY, 10, paint);
    		SimpleDateFormat formatter=new SimpleDateFormat("yyyy,MM,dd HH:mm:ss");
    		Date curDate=new Date(System.currentTimeMillis());
    		String str= formatter.format(curDate);
    		xyPosition="x:"+mX+",y:"+mY+",times:"+str;
    		ContentValues cv1=new ContentValues();
    		cv1.put("name", xyPosition);
    		pd1.insert(cv1);
    		setTitle("A = " + mAction + " ["+ mX + ","+ mY +"]");
    	}
    	@Override
    	public boolean onTouchEvent(MotionEvent event) {
    		mAction = event.getAction();
    		mX = event.getX();
    		mY = event.getY();
    		SimpleDateFormat formatter=new SimpleDateFormat("yyyy,MM,dd HH:mm:ss");
    		Date curDate=new Date(System.currentTimeMillis());
    		String str= formatter.format(curDate);
    		xyPosition="x:"+mX+",y:"+mY+",times:"+str;
    		ContentValues cv1=new ContentValues();
    		cv1.put("name", xyPosition);
    		pd1.insert(cv1);
    		Log.v(TAG,"Action = "+ mAction );
    		Log.v(TAG,"("+mX+","+mY+")" );
    		invalidate();
    		return true;
    	}
    }
    
    private SensorEventListener listener = new SensorEventListener() {
		public void onAccuracyChanged(Sensor arg0, int arg1) {
			
		}
		public void onSensorChanged(SensorEvent e) {
			gravity[0] = e.values[0];
			gravity[1] = e.values[1];
			gravity[2] = e.values[2];
			
			ContentValues cv1=new ContentValues();
			SimpleDateFormat formatter=new SimpleDateFormat("yyyy,MM,dd HH:mm:ss");
    		Date curDate=new Date(System.currentTimeMillis());
    		String str= formatter.format(curDate);
    		cv1.put("name1", gravity[0] +","+gravity[1]+","+gravity[2]+","+str);
    		pd2.insert1(cv1);
		}
	};
		
	@Override
	protected void onResume() {
		super.onResume();
		sensorManager.registerListener(listener, sensor,
				SensorManager.SENSOR_DELAY_NORMAL);
	}

	@Override
	protected void onStop() {
		super.onStop();
		sensorManager.unregisterListener(listener);
	}
}
