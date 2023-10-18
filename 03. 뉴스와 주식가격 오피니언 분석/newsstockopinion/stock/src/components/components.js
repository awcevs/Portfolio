import React from "react"
import { useNavigate } from "react-router-dom";

function SearchBar() {
    const navigate = useNavigate();
    function Event(e) {
        e.preventDefault();
        navigate('/search');
        //alert('클릭');
    }
    return (
        <div style={ { width:'100%',height:'30px',justifyContent:'center',display:'flex',position:'fixed',padding:'10px' } }>
            <input type="text" style={ { width:'300px' } }></input>
            <button type="button" onClick={Event}>검색</button>
        </div>
    )
}

function BtnTop() {
    const navigate = useNavigate();
    function Event(e) {
        e.preventDefault();
        navigate('/Top');
        //alert('클릭');
    }
    return (
        //<div style={ {width:'100px',height:'50px',border:'1px solid black', borderRadius:'5px'} } onClick={Event}>상위종목</div>
        <div style={ { margin:'10px' } }>
            <button type="button" onClick={Event} style={ { height:'35px' } }>상위종목</button>
        </div>
    )
}

function BtnMain() {
    const navigate = useNavigate();
    function Event(e) {
        e.preventDefault();
        navigate('/');
        //alert('클릭');
    }
    return (
        <div style={ { margin:'10px' } }>
            <button type="button" onClick={Event} style={ { height:'35px' } }>메인화면</button>
        </div>
    )
}

export { SearchBar, BtnTop, BtnMain }