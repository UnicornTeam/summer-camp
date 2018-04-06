package com.example.traffic_light_map_show.object;

public class Person_object {
	private Integer id;  
    private String name;  
   
	public Person_object(Integer id, String name) {
		super();
		this.id = id;
		this.name = name;
		
	}
	public Person_object(String name) {
		super();
		this.name = name;
		
	}
	public Person_object(){
		super();
	}
	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
}
