import React from "react"
import { SearchBar, BtnTop, BtnMain } from '../components/components'

function Main() {
    return (
      <>
        <SearchBar/>
        <div style={ { margin:'0 auto', maxWidth:'600px', paddingTop:'50px' } }>
          <div style={ { display:'flex' } }>
            <div style={ { width:'300px' } }>
              <table>
                <tr>
                  <td colSpan={4} style={ { textAlign:'left' } }>
                    <h2>오늘의 증시</h2>
                  </td>
                </tr>
                <tr>
                  <td className='text-left'>코스피</td>
                  <td className='text-right'>2499.50</td>
                  <td className='text-right'>9.41</td>
                  <td className='text-right'>-0.43%</td>
                </tr>
                <tr>
                  <td className='text-left'>코스닥</td>
                  <td className='text-right'>845.22</td>
                  <td className='text-right'>12.15</td>
                  <td className='text-right'>-1.34%</td>
                </tr>
                <tr>
                  <td className='text-left'>코스피 200</td>
                  <td className='text-right'>331.59</td>
                  <td className='text-right'>0.43</td>
                  <td className='text-right'  >-0.09%</td>
                </tr>
              </table>
            </div>
            <div style={ { width:'300px' } }>
              <table>
                <tr>
                  <td colSpan={4} style={ { textAlign:'left' } }>
                    <h2>TOP 종목</h2>
                  </td>
                </tr>
                <tr>
                  <td className='text-left'>코스피</td>
                  <td className='text-right'>2499.50</td>
                  <td className='text-right'>9.41</td>
                  <td className='text-right'>-0.43%</td>
                </tr>
                <tr>
                  <td className='text-left'>코스닥</td>
                  <td className='text-right'>845.22</td>
                  <td className='text-right'>12.15</td>
                  <td className='text-right'>-1.34%</td>
                </tr>
                <tr>
                  <td className='text-left'>코스피 200</td>
                  <td className='text-right'>331.59</td>
                  <td className='text-right'>0.43</td>
                  <td className='text-right'  >-0.09%</td>
                </tr>
              </table>
            </div>
          </div>
          <div>
            <table>
              <tr>
                <td colSpan={3} style={ { width:'600px' } }>
                  <h2>관심종목</h2>
                </td>
              </tr>
              <tr>
                <td style={ { width:'75px' } }>추가버튼</td>
                <td>종목명</td>
                <td>분석</td>
              </tr>
              <tr>
                <td>추가버튼</td>
                <td>종목명</td>
                <td>분석</td>
              </tr>
              <tr>
                <td>추가버튼</td>
                <td>종목명</td>
                <td>분석</td>
              </tr>
              <tr>
                <td>추가버튼</td>
                <td>종목명</td>
                <td>분석</td>
              </tr>
              <tr>
                <td>추가버튼  </td>
                <td>종목명</td>
                <td>분석</td>
              </tr>
            </table>
          </div>
        </div>
        <div className="btns">
          <BtnTop/>
        </div>
      </>
    );
};

export default Main;