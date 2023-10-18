package cteam.dto;

import java.util.ArrayList;
import cteam.dao.DBManager;
import cteam.vo.ChatVO;

public class ChatDTO extends DBManager
{
	public void Insert(ChatVO vo)
	{
		this.DBOpen();
		
		String sql = "";
		
		sql  = "insert ";
		sql += "	into chat(id,cnote) values( ";
		sql += "	'" + sRep(vo.getId())    + "', ";
		sql += "	'" + sRep(vo.getCnote()) + "') ";
		this.RunSQL(sql);
		
		this.DBClose();
		return;
	};
	
	public ChatVO Read(String cno)
	{
		ChatVO vo = null;
		this.DBOpen();
		String sql = "";
		sql  = "select ";
		sql += "	cno,id,cnote, ";
		sql += "	(select nick from user where id = chat.id) as nick ";
		sql += "from ";
		sql += "	chat ";
		sql += "where ";
		sql += "	cno = " + cno + " ";
		this.RunSelect(sql);
		if(this.Next() == true)
		{
			vo = new ChatVO();
			vo.setCno(this.getValue("cno"));
			vo.setNick(this.getValue("nick"));
			vo.setCnote(this.getValue("cnote").replace("<", "&lt;"));
			vo.setCnote(vo.getCnote().replace(">","&gt;"));
		}
		this.DBClose();
		return vo;
	}
	
	public ArrayList<ChatVO> List(String cno)
	{
		ArrayList<ChatVO> list = new ArrayList<ChatVO>();
		
		this.DBOpen();
		
		String sql = "";
		sql  = "select "; 
		sql += "	cno,id,cnote, "; 
		sql += "	(select nick from user where id = chat.id) as nick "; 
		sql += "from "; 
		sql += "	chat ";
		sql += "where cno > " + cno;
		this.RunSelect(sql);
		
		while(this.Next() == true)
		{
			ChatVO vo = new ChatVO();
			vo.setCno(this.getValue("cno"));
			vo.setId(this.getValue("id"));
			vo.setCnote(this.getValue("cnote").replace('"', '\"'));
			vo.setNick(this.getValue("nick"));
			list.add(vo);
		}
		
		this.DBClose();
		
		return list;
	}
	
}
