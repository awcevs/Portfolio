import React, { useEffect } from 'react';
import { SearchBar, BtnTop, BtnMain } from '../components/components'

function Test() {
    function stockindex() {
        fetch("http://localhost:5000/stockindex").then(
            // response 객체의 json() 이용하여 json 데이터를 객체로 변화
            res => res.json()
        ).then(
            // 데이터를 콘솔에 출력
            (json) => {
                obj = json
                console.log(obj)
            }
        )
    }
    let obj = {}
    return (
        <>
            <div>
                <h2>
                    테스트
                </h2>
            </div>
            <div>
                <table>
                    <thead>
                        <tr>
                            <td colSpan={4} style={ { textAlign:'left' } }>
                            <h2>오늘의 증시</h2>
                            </td>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td className='text-left' style={ { width:'90px',borderRight:'1px solid black' } }>코스피</td>
                            <td className='text-right'>{obj['kospi']['종가']}</td>
                            <td className='text-right'>{  }</td>
                            <td className='text-right'>{  }</td>
                        </tr>
                        <tr>
                            <td className='text-left' style={ { borderRight:'1px solid black' } }>코스닥</td>
                            <td className='text-right'>845.22</td>
                            <td className='text-right'>12.15</td>
                            <td className='text-right'>-1.34%</td>
                        </tr>
                        <tr>
                            <td className='text-left' style={ { borderRight:'1px solid black' } }>코스피 200</td>
                            <td className='text-right'>331.59</td>
                            <td className='text-right'>0.43</td>
                            <td className='text-right'  >-0.09%</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div className="btns">
                <BtnTop/>
                <BtnMain/>
            </div>
        </>
    );
};

export default Test;