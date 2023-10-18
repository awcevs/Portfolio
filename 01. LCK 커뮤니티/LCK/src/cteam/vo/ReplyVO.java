package cteam.vo;

public class ReplyVO
{
	protected String rno;      //댓글번호
	protected String bno;      //게시글번호
	protected String id;       //아이디
	protected String rnote;    //댓글내용
	protected String rblcount; //댓글신고누적
	protected String nick;     //작성자 닉네임
	protected String team;     //작성자 팀
	protected String position; //작성자 포지션
	
	
	
	
	
	
	public String getNick()		{	return nick;		}
	public String getRno()		{	return rno;			}
	public String getBno()		{	return bno;			}
	public String getId()		{	return id;			}
	public String getRnote()	{	return rnote;		}
	public String getRblcount()	{	return rblcount;	}
	public String getTeam()		{	return team;		}
	public String getPosition() {	return position;	}
	
	public void setRno(String rno)				{	this.rno = rno;				}
	public void setBno(String bno)				{	this.bno = bno;				}
	public void setId(String id)				{	this.id = id;				}
	public void setRnote(String rnote)			{	this.rnote = rnote;			}
	public void setRblcount(String rblcount)	{	this.rblcount = rblcount;	}
	public void setNick(String nick)			{	this.nick = nick;			}
	public void setTeam(String team) 			{	this.team = team;			}
	public void setPosition(String position) 	{	this.position = position;	}
	

}
