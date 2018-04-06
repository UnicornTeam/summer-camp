package com.example.traffic_light_map_show.dao;

import java.util.List;

import android.content.ContentValues;

import com.example.traffic_light_map_show.object.Person_object;

public interface PersonDao {
	
	boolean insert(ContentValues values);

	boolean update(ContentValues values, Integer id);
	
	Person_object findUserByNicheng(String[] niCheng);

	List<Person_object> findByName();
	
	public List<Person_object> findByName1() ;
	
	public boolean insert1(ContentValues values);
}