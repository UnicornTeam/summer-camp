package com.example.drt_3axis_acc;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.List;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.Toast;

import com.example.traffic_light_map_show.dao.PersonDao;
import com.example.traffic_light_map_show.dao.PersonDaoImpl1;
import com.example.traffic_light_map_show.object.Person_object;
import com.test.motionevent.MotionEventActivity;
import com.test.motionevent.R;


public class MainActivity1 extends Activity {
	private Button btn1;
	private Button btn3;
	private Button btn4;
	PersonDao pd1;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		// TODO Auto-generated method stub
		super.onCreate(savedInstanceState);
		setContentView(R.layout.mainactivity1);
		btn1=(Button)this.findViewById(R.id.button1_1);
		btn3=(Button)this.findViewById(R.id.button1_3);
		btn4=(Button)this.findViewById(R.id.button1_4);
		pd1=new PersonDaoImpl1(getApplicationContext());
		btn1.setOnClickListener(new OnClickListener() {
			
			public void onClick(View arg0) {
				// TODO Auto-generated method stub
			Intent intent=new Intent(MainActivity1.this,MotionEventActivity.class);
			startActivity(intent);
			}
		});
//		btn2.setOnClickListener(new OnClickListener() {
//			
//			public void onClick(View arg0) {
//				// TODO Auto-generated method stub
//			Intent intent1=new Intent(MainActivity1.this,MainActivity2.class);
//			startActivity(intent1);
//			}
//		});
		btn3.setOnClickListener(new OnClickListener() {
			
			public void onClick(View arg0) {
				// TODO Auto-generated method stub
				String ip="192.168.3.3";
				int port=1819;
//				Toast.makeText(getApplicationContext(), "11", Toast.LENGTH_SHORT).show();
				try 
				{
					List<Person_object> a=pd1.findByName();
					List<Person_object> a1=pd1.findByName1();
						String msg="";
						for(int i=0;i<a.size();i++){
							msg+=a.get(i).getName()+"  ";
						}
						for(int i=0;i<a1.size();i++){
							msg+=a1.get(i).getName()+"   ";
						}
						SendMsg(ip,port,msg);
				}
			 catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			 	}
			}
		});
//		btn4.setOnClickListener(new OnClickListener() {
//			
//			public void onClick(View arg0) {
//				// TODO Auto-generated method stub
//				String ip="192.168.1.102";
//				int port=1818;
//				try 
//				{
//					List<Person_object> a=pd1.findByName1();
//						String msg = "";
//						for(int i=0;i<a.size();i++){
//							msg+=a.get(i).getName()+"   ";
//						}
//						SendMsg(ip,port,msg);
//				}
//			 catch (Exception e) {
//				// TODO Auto-generated catch block
//				e.printStackTrace();
//			 	}
//			}
//		});
	}
	 public void SendMsg(String ip,int port,String msg) throws UnknownHostException, IOException
	    {
	    	try
	    	{
	    	Socket socket=null;
	    	socket=new Socket(ip,port);
	    	BufferedWriter writer=new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
	    	writer.write(msg);
	    	writer.flush();
	    	writer.close();
	    	socket.close();
	    	}
	    	catch(UnknownHostException e)
	    	{
	    		e.printStackTrace();
	    	} catch (IOException e) 
	    	{
	    	    e.printStackTrace();
	        }
	    }
}
