import React, {useState} from 'react';
import {FaEdit, FaTrash} from 'react-icons/fa';
import Checkbox from '@mui/material/Checkbox';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';

const List = ({ items, removeItem, editItem }) => {
    return (
        <div className='grocery-list'>
            {items.map((item) => {
                const { id, title, price } = item;
                return (
                    <article className='grocery-item' key={id}>
                        <p className='title'>{title}</p>
                        <p className='price'>{price}</p>
                        <div className='btn-container'>
                            <button
                                type='button'
                                className='edit-btn'
                                onClick={() => editItem(id)}>
                                <FaEdit />
                            </button>
                            <button
                                type='button'
                                className='delete-btn'
                                onClick={() => removeItem(id)}>
                                <FaTrash />
                            </button>
                            {/*<div>*/}
                            {/*    <p>Exclude</p>*/}
                            {/*    <input type="checkbox" />*/}
                            {/*    <input type="checkbox" />*/}
                            {/*    <input type="checkbox" />*/}
                            {/*    <input type="checkbox" />*/}
                            {/*    <input type="checkbox" />*/}
                            {/*</div>*/}
                        </div>
                    </article>
                );
            })}
        </div>
    );
};

export default List;