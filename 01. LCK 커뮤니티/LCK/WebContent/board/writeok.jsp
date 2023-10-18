<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%@ include file="../include/header.jsp" %>
<%@ include file="../include/upload.jsp" %>
<%@ page import="java.util.*" %>
<%@ page import="java.io.*" %>
<%@ page import="java.net.URLEncoder" %>
<%@ page import="com.oreilly.servlet.MultipartRequest" %>
<%@ page import="com.oreilly.servlet.multipart.DefaultFileRenamePolicy" %>
<!-- 컨텐츠 영역 시작 ======================================== -->
<%

if(islogin == false)
{
	response.sendRedirect("../user/userlogin.jsp");
	return;
}


//업로드 가능한 최대 파일 크기 지정
int size = 10 * 1024 * 1024; //10 MB
MultipartRequest multi = new MultipartRequest(
	request,    //request 객체
	uploadPath, //파일 업로드 경로
	size,       //파일 최대 사이즈
	"utf-8",   //인코딩 방식
	new DefaultFileRenamePolicy() //중복 파일명 처리
);

String btitle   = multi.getParameter("btitle"); 
btitle = btitle.replace("<", "&lt;");
btitle = btitle.replace(">", "&gt;");
btitle = btitle.replace("\"", "&quot;");
String menu     = multi.getParameter("menu");
String bnote    = multi.getParameter("bnote");
bnote = bnote.replace("<", "&lt;");
bnote = bnote.replace(">", "&gt;");
bnote = bnote.replace("\"", "&quot;");
String youtube  = multi.getParameter("youtube");
String newslink = multi.getParameter("newslink");

//업로드 된 파일명 (논리파일명, 사용자가 업로드한 파일명)
String bfname = (String)multi.getFilesystemName("attach");
//랜덤 문자열 생성 (물리파일명, 실제 저장 파일명)
String bpname = UUID.randomUUID().toString();
//논리파일명을 물리파일명으로 변경
String srcName    = uploadPath + "\\" + bfname;
//System.out.println("논리파일명 : " + bfname);
String targetName = uploadPath + "\\" + bpname;
//System.out.println("물리파일명 : " + bpname);
File srcFile    = new File(srcName);
File targetFile = new File(targetName);
srcFile.renameTo(targetFile);

if(bfname == null)
{
	bfname = "";
	bpname = ""; //bpname은 bfname = null이여도 생성됨
}

//DB insert

BoardVO  vo  = new BoardVO();
BoardDTO dto = new BoardDTO();
vo.setBtitle(btitle);
vo.setId(login.getId());
vo.setBnote(bnote);
vo.setMenu(menu);
vo.setBfname(bfname);
vo.setBpname(bpname);
vo.setYoutube(youtube);
vo.setNewslink(newslink);

dto.Insert(vo);

response.sendRedirect("view.jsp?menu=" + menu + "&bno=" + vo.getBno()); //작성한 글 view 페이지로

%>
<!-- 컨텐츠 영역 종료 ======================================== -->
<%@ include file="../include/footer.jsp" %>