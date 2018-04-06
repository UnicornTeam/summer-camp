package com.example.traffic_light_map_show.dao;

import java.util.ArrayList;
import java.util.List;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;

import com.example.traffic_light_map_show.db.DbSqliteOpenHelper;
import com.example.traffic_light_map_show.object.Person_object;


public class PersonDaoImpl1 implements PersonDao {
	private DbSqliteOpenHelper dbsqliteOpenHelper;
	SQLiteDatabase db;

	public PersonDaoImpl1(Context context) {
		super();
		dbsqliteOpenHelper = new DbSqliteOpenHelper(context);
		db = dbsqliteOpenHelper.getWritableDatabase();
	}
	
	public boolean insert(ContentValues values) {
		db = dbsqliteOpenHelper.getWritableDatabase();
		// TODO Auto-generated method stub
		boolean flag = false;
		if (db.isOpen()) {
			long l = db.insert("person", null, values);
			if (l > 0) {
				flag = true;
			}
			db.close();
		}
		return flag;
	}
	
	public boolean insert1(ContentValues values) {
		db = dbsqliteOpenHelper.getWritableDatabase();
		// TODO Auto-generated method stub
		boolean flag = false;
		if (db.isOpen()) {
			long l = db.insert("person1", null, values);
			if (l > 0) {
				flag = true;
			}
			db.close();
		}
		return flag;
	}
	public boolean update(ContentValues values, Integer id) {
		db = dbsqliteOpenHelper.getWritableDatabase();
		boolean flag = false;
		if (db.isOpen()) {
			long l = db.update("person", values, "id=?",
					new String[] { id + "" });
			if (l > 0) {
				flag = true;
			}
			db.close();
		}
		return flag;
	}
	
	public Person_object findUserByNicheng() {
		db = dbsqliteOpenHelper.getWritableDatabase();
		// TODO Auto-generated method stub
		List<Person_object> persons = new ArrayList<Person_object>();
		// TODO Auto-generated method stub
		boolean flag = false;
		Person_object person = null;
		if (db.isOpen()) {
			Cursor l = db.query(true, "person", null,null,null, null, null, null, null);

			while (l.moveToNext()) {
				person = new Person_object();
				person.setId(l.getInt(l.getColumnIndex("id")));
				person.setName(l.getString(l.getColumnIndex("name")));
			}
		}
		db.close();
		return person;
	}
	
	public List<Person_object> findByName() {
		db = dbsqliteOpenHelper.getWritableDatabase();
		List<Person_object> persons = new ArrayList<Person_object>();
		// TODO Auto-generated method stub
		if (db.isOpen()) {
			Cursor l = db.query(true, "person", null,null,null, null, null, null, null);
			while (l.moveToNext()) {
				Person_object person = new Person_object();
				person.setId(l.getInt(l.getColumnIndex("id")));
				person.setName(l.getString(l.getColumnIndex("name")));
				persons.add(person);
			}
		}
		db.close();
		return persons;
	}

	public List<Person_object> findByName1() {
		db = dbsqliteOpenHelper.getWritableDatabase();
		List<Person_object> persons = new ArrayList<Person_object>();
		// TODO Auto-generated method stub
		if (db.isOpen()) {
			Cursor l = db.query(true, "person1", null,null,null, null, null, null, null);
			while (l.moveToNext()) {
				Person_object person = new Person_object();
				person.setId(l.getInt(l.getColumnIndex("id1")));
				person.setName(l.getString(l.getColumnIndex("name1")));
				persons.add(person);
			}
		}
		db.close();
		return persons;
	}
	public Person_object findUserByNicheng(String[] niCheng) {
		// TODO Auto-generated method stub
		return null;
	}

	

}
