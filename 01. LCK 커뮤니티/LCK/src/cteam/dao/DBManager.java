package cteam.dao;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DBManager
{
	private Connection conn;
	private Statement  stmt;
	private ResultSet  rs;
	
	public DBManager()
	{
		conn = null;
		stmt = null;
	}
	
	//드라이버 로딩 및 DB 연결 
	public boolean DBOpen()
	{
		//1. jdbc 라이브러리 로딩
		try
		{
			Class.forName("com.mysql.cj.jdbc.Driver");
		} catch (ClassNotFoundException e)
		{
			e.printStackTrace();
			return false;
		}
		//2. 데이터베이스에 연결
		String host = "jdbc:mysql://127.0.0.1:3306/cteam";
		host += "?useUnicode=true&characterEncoding=utf-8";
		host += "&serverTimezone=UTC";
		
		try
		{
			conn = DriverManager.getConnection(host,"root","ezen");
			stmt = conn.createStatement();
		} catch (SQLException e)
		{
			e.printStackTrace();
			return false;
		}
		System.out.println("데이터베이스 연결 성공");
		return true;
	}

//	//드라이버 로딩 및 DB 연결 
//	public boolean DBOpen(String dbName, String id, String pw)
//	{	
//		//1. jdbc 라이브러리 로딩
//		try
//		{
//			Class.forName("com.mysql.cj.jdbc.Driver");
//			//2. 데이터베이스에 연결
//			String host = "jdbc:mysql://127.0.0.1:3306/" + dbName;
//			host += "?useUnicode=true&characterEncoding=utf-8";
//			host += "&serverTimezone=UTC";
//			conn = DriverManager.getConnection(host,id,pw);
//			stmt = conn.createStatement();
//		} catch (ClassNotFoundException e)
//		{
//			e.printStackTrace();
//			return false;
//		} catch (SQLException e1)
//		{
//			e1.printStackTrace();
//			return false;
//		}
//		
//		System.out.println("데이터베이스 연결 성공");
//		return true;
//	}
	
	//DB 연결 닫기
	public void DBClose()
	{
		try
		{
			stmt.close();
			conn.close();
		} catch (SQLException e)
		{
			e.printStackTrace();
		}
	}
	
	//Insert, Delete, Update 실행
	public boolean RunSQL(String sql)
	{
		try
		{
			stmt.executeUpdate(sql);
		} catch (SQLException e)
		{
			e.printStackTrace();
			return false;
		}
		sql = sql.replace("\t", "");
		System.out.println(sql);
		return true;
	}
	
	//Select 실행
	public boolean RunSelect(String sql)
	{
		try
		{
			rs = stmt.executeQuery(sql);
		} catch (SQLException e)
		{
			e.printStackTrace();
			return false;
		}
		sql = sql.replace("\t", "");
		System.out.println(sql);
		return true;
	}
	
	//ResultSet을 Next 처리 -> ResultSet rs가 private임
	public boolean Next()
	{
		try
		{
			return rs.next();
		} catch (SQLException e)
		{
			e.printStackTrace();
			return false;
		}
	}
	
	//ResultSet에 getString 처리
	public String getValue(String column)
	{
		try
		{
			return rs.getString(column);
		} catch (SQLException e)
		{
			e.printStackTrace();
			return null;
		}
	}
	
	//작은 따옴표 변경
	public String sRep(String data)
	{
		if(data == null) return null;
		return data.replace("'", "''");
	}
}
