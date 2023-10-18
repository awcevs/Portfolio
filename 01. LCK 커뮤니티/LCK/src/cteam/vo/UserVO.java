package cteam.vo;

public class UserVO
{
	protected String id;       //아이디
	protected String pw;       //비밀번호
	protected String name;     //이름
	protected String nick;     //닉네임
	protected String team;     //팀
	protected String position; //포지션
	protected String email;    //이메일
	protected String joindate; //가입일자
	protected String userdiv;  //유저구분
	
	
	public String getId()		{		return id;			}
	public String getPw()		{		return pw;			}
	public String getName()		{		return name;		}
	public String getNick()		{		return nick;		}
	public String getTeam()		{		return team;		}
	public String getPosition()	{		return position;	}
	public String getEmail()	{		return email;		}
	public String getJoindate()	{		return joindate;	}
	public String getUserdiv()	{		return userdiv;		}
	
	public void setId(String id)				{	this.id = id;				}
	public void setPw(String pw)				{	this.pw = pw;				}
	public void setName(String name)			{	this.name = name;			}
	public void setNick(String nick)			{	this.nick = nick;			}
	public void setTeam(String team)			{	this.team = team;			}
	public void setPosition(String position)	{	this.position = position;	}
	public void setEmail(String email)			{	this.email = email;			}
	public void setJoindate(String joindate)	{	this.joindate = joindate;	}
	public void setUserdiv(String userdiv)		{	this.userdiv = userdiv;		}
	
	
	

}
