drop database cteam;

create database cteam;

use cteam;

create table user
(
id varchar(20) primary key comment '아이디',
pw varchar(200) comment '비밀번호',
name varchar(50) comment '이름',
nick varchar(6) comment '닉네임',
team varchar(4) comment '팀',
position varchar(3) comment '포지션',
email varchar(50) comment '이메일',
joindate datetime default now() comment '가입일자',
userdiv varchar(1) comment '회원구분'
);

create table board
(
bno int primary key auto_increment comment '글번호', 
btitle varchar(40) comment '제목',
bnote text comment '내용',
id varchar(20) comment '아이디',
wdate datetime default now() comment '작성일',
hit int default 0 comment '조회수',
gcount int default 0 comment '추천',
blcount int default 0 comment '신고',
bfname varchar(200) comment '논리파일명',
bpname varchar(200) comment '물리파일명',
menu varchar(1) comment '메뉴',
youtube varchar(11) comment '동영상ID',
newslink varchar(100) comment '뉴스링크',
foreign key(id) references user(id)
);

create table reply
(
rno int primary key auto_increment comment '댓글번호',
bno int comment '게시물번호',
id varchar(20) comment '작성자 아이디',
rnote text comment '댓글내용',
rblcount int default 0 comment '댓글신고',
foreign key(id) references user(id),
foreign key(bno) references board(bno)
);

create table service
(
sno int primary key auto_increment comment '신고번호',
id varchar(20) comment '아이디',
sdiv varchar(1) comment '신고구분',
bno int comment '글 번호',
rno int comment '댓글 번호',
foreign key(id) references user(id),
foreign key(bno) references board(bno),
foreign key(rno) references reply(rno)
);

create table chat
(
cno int primary key auto_increment comment '채팅번호',
id varchar(20) comment '아이디',
cnote text comment '채팅내용',
foreign key(id) references user(id)
);
