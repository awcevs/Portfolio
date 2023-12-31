package cteam.dto;

import cteam.vo.*;

import java.util.ArrayList;
//import cteam.dao.*;
import cteam.dao.DBManager;

public class BoardDTO extends DBManager
{
	//C:BoardVO객체를 DB에 저장(insert)한다.
	public void Insert(BoardVO vo)
	{
		this.DBOpen();
		String sql = "";
		sql  = "insert ";
		sql += "	into board (id,btitle,bnote,menu,bfname,bpname,youtube,newslink) values (";
		sql += "	'" + vo.getId()       + "', ";
		sql += "	'" + sRep(vo.getBtitle())   + "', "; 
		sql += "	'" + sRep(vo.getBnote())    + "', ";
		sql += "	'" + vo.getMenu()     + "', "; 
		sql += "	'" + sRep(vo.getBfname())   + "', "; 
		sql += "	'" + vo.getBpname()   + "', ";
		sql += "	'" + sRep(vo.getYoutube())  + "', ";
		sql += "	'" + sRep(vo.getNewslink()) + "') ";
		this.RunSQL(sql);
		
		//등록된 게시물의 번호를 얻는다
		sql = "select last_insert_id() as no ";
		this.RunSelect(sql);
		if( this.Next() == true )
		{
			vo.setBno(this.getValue("no"));
		}
		this.DBClose();
	}
	
	//R:DB에서 자료를 가져와서(select) BoardVO에 넣는다.
	//IsHit: true - 조회수 증가, false - 조회수 증가하지 않음
	public BoardVO Read(String bno, boolean IsHit)
	{
		BoardVO vo = null;
		this.DBOpen();
		String sql = "";
		sql  = "select ";
		sql += "	id,btitle,menu,bnote,bfname,bpname,wdate,hit,gcount,blcount,youtube,newslink, ";
		sql += "	(select nick from user where id = board.id) as nick, ";
		sql += "	(select nick from user where id = board.id) as nick, ";
		sql += "	(select team from user where id = board.id) as team,";
		sql += "	(select position from user where id = board.id) as position ";
		sql += "from ";
		sql += "	board ";
		sql += "where ";
		sql += "	bno = '" + bno + "' ";
		this.RunSelect(sql);
		if(this.Next() == true)
		{
			//게시물 정보가 있음
			vo = new BoardVO();
			vo.setBno(bno);
			vo.setId(this.getValue("id"));
			vo.setBtitle(this.getValue("btitle"));
			vo.setMenu(this.getValue("menu"));
			vo.setBnote(this.getValue("bnote"));
			vo.setBfname(this.getValue("bfname"));
			vo.setBpname(this.getValue("bpname"));
			vo.setWdate(this.getValue("wdate"));
			vo.setHit(this.getValue("hit"));
			vo.setNick(this.getValue("nick"));
			vo.setTeam(this.getValue("team"));
			vo.setPosition(this.getValue("position"));
			vo.setGcount(this.getValue("gcount"));
			vo.setBlcount(this.getValue("blcount"));
			vo.setYoutube(this.getValue("youtube"));
			vo.setNewslink(this.getValue("newslink"));
			//조회수 증가 시킨다
			if(IsHit == true)
			{
				sql = "update board set hit = hit + 1 where bno = '" + bno + "' ";
				this.RunSQL(sql);
			}

		}
		this.DBClose();
		return vo;
	}
	
	//추천 기능
	public void GoodUpdate(BoardVO vo)
	{
		this.DBOpen();
		String sql = "";
		sql = "update board set gcount = gcount + 1 where bno = " + vo.getBno();
		this.RunSQL(sql);
		this.DBClose();
	}
	
	//신고기능
	public void BlockUpdate(BoardVO vo)
	{
		this.DBOpen();
		String sql = "";
		sql = "update board set blcount = blcount + 1 where bno = " + vo.getBno();
		this.RunSQL(sql);
		this.DBClose();
	}
	
	//U:BoardVO객체를 DB에 변경(update)한다.
	public void Update(BoardVO vo)
	{
		this.DBOpen();

		String sql = "";
		
		sql  = "update ";
		sql += "	board ";
		sql += "set ";
		sql += "	btitle = '"   + sRep(vo.getBtitle())   + "', ";
		sql += "	menu = '"     + vo.getMenu()     + "', ";
		sql += "	youtube = '"  + vo.getYoutube()  + "', ";
		sql += "	newslink = '" + vo.getNewslink() + "', ";
		if(!vo.getBfname().equals(""))
		{
			//글이 수정되기 전 첨부파일이 있을 때, 그 첨부파일을 그대로 업데이트 
			sql += "bnote = '"  + sRep(vo.getBnote())  + "', ";
			sql += "bfname = '" + sRep(vo.getBfname()) + "', ";
			sql += "bpname = '" + vo.getBpname() + "'  ";
		}else
		{
			sql += "bnote = '" + sRep(vo.getBnote()) + "' ";
		}
		sql += "where ";
		sql += "	bno = '" + vo.getBno() + "' ";
		this.RunSQL(sql);
		this.DBClose();
	}
	
	//D:BoardVO객체를 이용하여 DB에서 삭제한다.
	public void Delete(String bno)
	{
		this.DBOpen();
		String sql = "";
		sql = "delete from service where bno = '" + bno + "' ";
		this.RunSQL(sql);
		sql = "delete from reply where bno = '" + bno + "' ";
		this.RunSQL(sql);
		
		sql = "delete from board where bno = '" + bno + "' ";
		this.RunSQL(sql);
		this.DBClose();
	}
	
	//R:전체 게시물 갯수를 얻는다.
	//menu : 뉴스 : N / 대회 : T / 하이라이트 : H / 자유 : F / 질답 : Q / 정보 : I / 파티 : P / 이동 : M
	public int GetTotal(String menu)
	{
		int total = 0;
		
		this.DBOpen();
		String sql = "";
		sql  = "select count(*) as total "; 
		sql += "from board ";
		sql += "where menu = '" + menu + "' ";
		this.RunSelect(sql);
		if(this.Next() == true)
		{
			total = Integer.parseInt(this.getValue("total"));
		}
		this.DBClose();
		return total;
	}
	
	public int GetTotal(String menu,String opt, String word)
	{
		int total = 0;
		
		this.DBOpen();
		String sql = "";
		sql  = "select count(*) as total "; 
		sql += "from board ";
		sql += "where menu = '" + menu + "' and " + opt + " like '%" + word + "%' ";
		this.RunSelect(sql);
		if(this.Next() == true)
		{
			total = Integer.parseInt(this.getValue("total"));
		}
		this.DBClose();
		return total;
	}
	
	public ArrayList<BoardVO> List(String menu)
	{
		
		ArrayList<BoardVO> list = new ArrayList<BoardVO>();
		
		this.DBOpen();
		String sql = "";
		sql  = "select ";
		sql += "	bno,btitle,menu,hit,youtube,gcount,blcount,youtube,bfname,bpname, ";
		sql += "	date_format(wdate, '%m-%d') as wdate,";
		sql += "	(select nick from user where id = board.id) as nick,";
		sql += "	(select team from user where id = board.id) as team,";
		sql += "	(select position from user where id = board.id) as position,";
		sql += "	(select count(*) from reply where bno = board.bno) as rcount ";
		sql += "from ";
		sql += "	board ";
		sql += "where ";
		sql += "	menu = '" + menu + "' and id in (select id from user where userdiv='2') ";
		sql += "order by bno desc ";
		sql += "limit 0,3";
		this.RunSelect(sql);
		while(this.Next() == true)
		{
			BoardVO vo = new BoardVO();
			vo.setBno(this.getValue("bno"));
			vo.setBtitle(this.getValue("btitle"));
			vo.setMenu(this.getValue("menu"));
			vo.setWdate(this.getValue("wdate"));
			vo.setHit(this.getValue("hit"));
			vo.setNick(this.getValue("nick"));
			vo.setRcount(this.getValue("rcount"));
			vo.setTeam(this.getValue("team"));
			vo.setPosition(this.getValue("position"));
			vo.setBfname(this.getValue("bfname"));
			vo.setBpname(this.getValue("bpname"));
			vo.setGcount(this.getValue("gcount"));
			vo.setBlcount(this.getValue("blcount"));
			vo.setYoutube(this.getValue("youtube"));
			
			list.add(vo);
		}
		this.DBClose();
		return list;
	}
	
	//R:DB에서 자료 목록을 가져와서(select) BoardVO LIST에 넣는다.
	//menu : 뉴스 : N / 대회 : T / 하이라이트 : H / 자유 : F / 질답 : Q / 정보 : I / 파티 : P / 이동 : M
	public ArrayList<BoardVO> List(String menu, int PageNo)
	{
		ArrayList<BoardVO> list = new ArrayList<BoardVO>();
		
		int startNo = (PageNo - 1) * 10; //시작번호
		
		this.DBOpen();
		String sql = "";
		sql  = "select ";
		sql += "	bno,btitle,menu,hit,youtube,gcount,blcount,youtube,bfname,bpname, ";
		sql += "	date_format(wdate, '%m-%d') as wdate,";
		sql += "	(select nick from user where id = board.id) as nick,";
		sql += "	(select team from user where id = board.id) as team,";
		sql += "	(select position from user where id = board.id) as position,";
		sql += "	(select count(*) from reply where bno = board.bno) as rcount ";
		sql += "from ";
		sql += "	board ";
		sql += "where ";
		sql += "	menu = '" + menu + "'  and id in (select id from user where userdiv='1')  ";
		sql += "order by bno desc ";
		sql += "limit " + startNo + ",10";
		this.RunSelect(sql);
		System.out.println(sql);
		while(this.Next() == true)
		{
			BoardVO vo = new BoardVO();
			vo.setBno(this.getValue("bno"));
			vo.setBtitle(this.getValue("btitle"));
			vo.setMenu(this.getValue("menu"));
			vo.setWdate(this.getValue("wdate"));
			vo.setHit(this.getValue("hit"));
			vo.setNick(this.getValue("nick"));
			vo.setRcount(this.getValue("rcount"));
			vo.setTeam(this.getValue("team"));
			vo.setPosition(this.getValue("position"));
			vo.setBfname(this.getValue("bfname"));
			vo.setBpname(this.getValue("bpname"));
			vo.setGcount(this.getValue("gcount"));
			vo.setBlcount(this.getValue("blcount"));
			vo.setYoutube(this.getValue("youtube"));
			
			list.add(vo);
		}
		this.DBClose();
		return list;
	}
	
	//검색 리스트 불러오기
	public ArrayList<BoardVO> ListSearch(String menu, int PageNo, String scOpt, String scWord)
	{
		ArrayList<BoardVO> list = new ArrayList<BoardVO>();
		
		int startNo = (PageNo - 1) * 10; //시작번호
		
		this.DBOpen();
		String sql = "";
		sql  = "select bno,btitle,menu,hit,youtube,gcount,blcount,youtube,bfname,bpname, ";
		sql += "date_format(wdate, '%m-%d') as wdate, ";
		sql += "(select nick from user where id = board.id) as nick, ";
		sql += "(select team from user where id = board.id) as team, ";
		sql += "(select position from user where id = board.id) as position, ";
		sql += "(select count(*) from reply where bno = board.bno) as rcount ";
		sql += "from board ";
		sql += "where menu = '" + menu + "' and " + scOpt + " like '%" + scWord + "%' ";
		sql += "order by bno desc ";
		sql += "limit " + startNo + ",10";
		this.RunSelect(sql);
		
		while(this.Next() == true)
		{
			BoardVO vo = new BoardVO();
			vo.setBno(this.getValue("bno"));
			vo.setBtitle(this.getValue("btitle"));
			vo.setMenu(this.getValue("menu"));
			vo.setWdate(this.getValue("wdate"));
			vo.setHit(this.getValue("hit"));
			vo.setNick(this.getValue("nick"));
			vo.setRcount(this.getValue("rcount"));
			vo.setTeam(this.getValue("team"));
			vo.setPosition(this.getValue("position"));
			vo.setBfname(this.getValue("bfname"));
			vo.setBpname(this.getValue("bpname"));
			vo.setGcount(this.getValue("gcount"));
			vo.setBlcount(this.getValue("blcount"));
			vo.setYoutube(this.getValue("youtube"));
			
			list.add(vo);
		}
		this.DBClose();
		return list;
	}
	//최신글 불러오기
	//1 : 대회 분류, 2 : 커뮤니티 분류
	public ArrayList<BoardVO> ListRecent(String div)
	{
		ArrayList<BoardVO> list = new ArrayList<BoardVO>();
		
		this.DBOpen();
		String sql = "";
		sql  = "select ";
		sql += "	bno,btitle,menu, ";
		sql += "	(select count(*) from reply where bno = board.bno) as rcount ";
		sql += "from ";
		sql += "	board ";
		if(div.equals("1")) sql += "where menu = 'N' or menu = 'T' or menu='H' ";
		if(div.equals("2")) sql += "where menu = 'F' or menu = 'Q' or menu='I' or menu='P' or menu='M' ";
		sql += "order by bno desc ";
		sql += "limit 0,10";
		this.RunSelect(sql);
		
		while(this.Next() == true)
		{
			BoardVO vo = new BoardVO();
			vo.setBno(this.getValue("bno"));
			vo.setBtitle(this.getValue("btitle"));
			vo.setMenu(this.getValue("menu"));
			vo.setRcount(this.getValue("rcount"));
			
			list.add(vo);
		}
		this.DBClose();
		return list;
	}	
	
	//인기글 불러오기
	public ArrayList<BoardVO> ListPopular()
	{
		ArrayList<BoardVO> list = new ArrayList<BoardVO>();
		
		this.DBOpen();
		String sql = "";
		sql  = "select ";
		sql += "	bno,btitle,menu ";
		sql += "from ";
		sql += "	board ";
		sql += "where ";
		sql += "	blcount < 10 ";
		sql += "order by gcount desc ";
		sql += "limit 0,10";
		this.RunSelect(sql);
		
		while(this.Next() == true)
		{
			BoardVO vo = new BoardVO();
			vo.setBno(this.getValue("bno"));
			vo.setBtitle(this.getValue("btitle"));
			vo.setMenu(this.getValue("menu"));
			
			list.add(vo);
		}
		this.DBClose();
		return list;
	}	
}
