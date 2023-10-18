import React from 'react';
import { SearchBar, BtnTop, BtnMain } from '../components/components'

function Search() {
    return (
        <>
            <div>
                <h2>
                    검색
                </h2>
            </div>
            <div className="btns">
                <BtnTop/>
                <BtnMain/>
            </div>
        </>
    );
};

export default Search;