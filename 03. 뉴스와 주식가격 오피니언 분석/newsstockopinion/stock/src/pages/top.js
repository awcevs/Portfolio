import React from 'react';
import { SearchBar, BtnTop, BtnMain } from '../components/components'

function Top() {
    return (
        <>
            <div>
                <h2>
                    상위종목
                </h2>
            </div>
            <div className="btns">
                <BtnMain/>
            </div>
        </>
    );
};

export default Top;