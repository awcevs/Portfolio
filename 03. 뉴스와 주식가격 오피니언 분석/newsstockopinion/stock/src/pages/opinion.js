import React from 'react';
import { SearchBar, BtnTop, BtnMain } from '../components/components'

function Opinion() {
    return (
        <>
            <div>
                <h2>
                    분석
                </h2>
            </div>
            <div className="btns">
                    <BtnTop/>
                    <BtnMain/>
            </div>
        </>
    );
};

export default Opinion;