package cteam.dto;

import java.util.ArrayList;

import cteam.dao.DBManager;
import cteam.vo.ReplyVO;

public class ReplyDTO extends DBManager
{
		//´ñ±Û µî·Ï
		public void Insert(ReplyVO vo) 
		{
			this.DBOpen();
			
			String sql = "";
			sql  = "insert into reply(id,bno,rnote) ";
			sql += "values ('" + sRep(vo.getId()) + "',";
			sql	+= "'" + vo.getBno() + "',";
			sql += "'"+ sRep(vo.getRnote()) + "')";
			this.RunSQL(sql);
			System.out.println(sql);
			sql = "select last_insert_id() as no ";
			this.RunSelect(sql);
			
			if(this.Next() == true )
			{
				vo.setRno(this.getValue("no"));
			}
			
			this.DBClose();
		}
		
		//´ñ±Û Á¤º¸ °¡Á®¿À±â
		public ReplyVO Read(String rno) 
		{
			ReplyVO vo = null;
			this.DBOpen();
			String sql = "";
			sql  = "select ";
			sql += "bno,id,rnote, ";
			sql += "(select nick from user where id = reply.id) as nick, ";
			sql += "(select team from user where id = reply.id) as team, ";
			sql += "(select position from user where id = reply.id) as position ";
			sql += "from reply ";
			sql += "where rno='" + rno + "'";
			this.RunSelect(sql);
			System.out.println(sql);
			if(this.Next() == true)
			{
				vo = new ReplyVO();
				vo.setRno(rno);
				vo.setBno(this.getValue("bno"));
				vo.setId(this.getValue("id"));
				vo.setRnote(this.getValue("rnote"));
				vo.setNick(this.getValue("nick"));
				vo.setTeam(this.getValue("team"));
				vo.setPosition(this.getValue("position"));
			}
			this.DBClose();
			return vo;
		}
		
		//´ñ±Û »èÁ¦
		public void Delete(String rno)
		{
			this.DBOpen();
			
			String sql = "";
			sql = "delete from service where rno='"+ rno + "'";
			System.out.println(sql);
			this.RunSQL(sql);
			sql = "delete from reply where rno='"+ rno + "'";
			System.out.println(sql);
			this.RunSQL(sql);
			
			this.DBClose();
		}
		
		//´ñ±Û ½Å°í ´©Àû
		public void RblUpdate(ReplyVO vo)
		{
			this.DBOpen();
			String sql = "";
			sql  = "update reply set ";
			sql += "rblcount = rblcount + 1 where rno = " + vo.getRno();
			this.RunSQL(sql);
			this.DBClose();
		}
		
		//´ñ±Û ¼öÁ¤
		public void Update(ReplyVO vo)
		{
			this.DBOpen();
			
			String sql = "";
			
			sql  = "update ";
			sql += "	reply ";
			sql += "set ";
			sql += "	rnote = '" + sRep(vo.getRnote()) + "' ";
			sql += "where ";
			sql += "	rno = " + vo.getRno();
			System.out.println(sql);
			this.RunSQL(sql);
			
			this.DBClose();
		}
		
		//´ñ±Û ¸®½ºÆ®
		public ArrayList<ReplyVO> List(String bno)
		{
			ArrayList<ReplyVO> list = new ArrayList<ReplyVO>();
			
//			int limitStart = (PageNo - 1) * 10;
			
			this.DBOpen();
			
			String sql = "";
			
			sql  = "select ";
			sql += "	rno,id,rnote,rblcount, ";
			sql += "	(select nick from user where id = reply.id) as nick, ";
			sql += "	(select team from user where id = reply.id) as team, ";
			sql += "	(select position from user where id = reply.id) as position ";
			sql += "from ";
			sql += "	reply ";
			sql += "where ";
			sql += "	bno = " + bno + " ";
//			sql += "limit " + limitStart + " ,10" ;
			this.RunSelect(sql);
			while(this.Next() == true)
			{
				ReplyVO vo = new ReplyVO();
				vo.setRno(this.getValue("rno"));
				vo.setId(this.getValue("id"));
				vo.setRnote(this.getValue("rnote"));
				vo.setNick(this.getValue("nick"));
				vo.setTeam(this.getValue("team"));
				vo.setPosition(this.getValue("position"));
				vo.setRblcount(this.getValue("rblcount"));
				list.add(vo);
			}
			
			this.DBClose();
			
			return list;
		}
}
