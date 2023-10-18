import React from "react"
import { BrowserRouter, Routes, Route, Link, Switch } from "react-router-dom";
import './App.css';
import Main from './pages/main'
import Search from './pages/search'
import Top from './pages/top'
import Opinion from './pages/opinion'
import News from './pages/news'
import Test from './pages/test'

function App() {
  return (
      <div className="App">
        <Routes>
          <Route path="/" element={ <Main/> }/>
          <Route path="/main" element={ <Main/> }/>
          <Route path="/search" element={ <Search/> }/>
          <Route path="/top" element={ <Top/> }/>
          <Route path="/opinion" element={ <Opinion/> }/>
          <Route path="/news" element={ <News/> }/>
          <Route path="/test" element={ <Test/> }/>
        </Routes>
      </div>
  );
}

export default App;
