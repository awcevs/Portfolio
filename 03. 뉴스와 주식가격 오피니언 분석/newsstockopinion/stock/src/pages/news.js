import React from 'react';
import { SearchBar, BtnTop, BtnMain } from '../components/components'

function News() {
    return (
        <>
            <div>
                <h2>
                    뉴스
                </h2>
            </div>
            <div className="btns">
                <BtnTop/>
                <BtnMain/>
            </div>
        </>
    );
};

export default News;