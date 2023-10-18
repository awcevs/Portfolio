<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%@ page import="cteam.dao.*" %>    
<%@ page import="cteam.dto.*" %>    
<%@ page import="cteam.vo.*" %>    
<%
	String bno = request.getParameter("bno");
	UserVO login = (UserVO)session.getAttribute("login");
	String sdiv = request.getParameter("sdiv");
	String id = login.getId();
	String rno = request.getParameter("rno");
	
	BoardDTO   bdto = new BoardDTO();
	ReplyDTO   rdto = new ReplyDTO();
	ServiceDTO sdto = new ServiceDTO();
	ServiceVO  svo  = new ServiceVO();
	
	//게시글
	if(rno == null)
	{
		if(sdto.Bcheck(bno, sdiv, id) == true)
		{
			svo.setBno(bno);
			svo.setId(id);
			svo.setSdiv(sdiv);
			sdto.InsertB(svo);
			BoardVO bvo = bdto.Read(bno, false);
			if(sdiv.equals("0"))
			{
				bdto.GoodUpdate(bvo);
				bvo = bdto.Read(bno, false);
				out.print(bvo.getGcount());
			}
			if(sdiv.equals("1"))
			{
				bdto.BlockUpdate(bvo);
				bvo = bdto.Read(bno, false);
				out.print(bvo.getBlcount());
			}
		}else
		{
			out.print("N");
		}
	}
	
	//댓글
	if(sdiv == null)
	{
		if(sdto.Rcheck(rno, id) == true)
		{
			svo.setRno(rno);
			svo.setId(id);
			sdto.InsertR(svo);
			ReplyVO rvo = rdto.Read(rno);
			rdto.RblUpdate(rvo);
			rvo = rdto.Read(rno);
			out.print(rvo.getRblcount());
		}else
		{
			out.print("N");
		}
	}
%>
