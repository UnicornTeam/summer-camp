package com.example.traffic_light_map_show.db;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.util.Log;

public class DbSqliteOpenHelper extends SQLiteOpenHelper {
	private static final String tag="DBSQLiteHelper";
	private static final String name="people1.db";
	private static final int version=1;
	public DbSqliteOpenHelper(Context context) {
		super(context, name, null, version);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void onCreate(SQLiteDatabase db) {
		// TODO Auto-generated method stub
		db.execSQL("Create table person(id integer primary key autoincrement,name varchar(20))");
		db.execSQL("Create table person1(id1 integer primary key autoincrement,name1 varchar(20))");
	}


	@Override
	public void onUpgrade(SQLiteDatabase arg0, int arg1, int arg2) {
		// TODO Auto-generated method stub
		
	}

}
