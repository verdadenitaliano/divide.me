import React, { useState, useEffect } from 'react';
import List from './List';
import Alert from './Alert';
const getLocalStorage = () => {
  let list = localStorage.getItem('list');
  if (list) {
    return (list = JSON.parse(localStorage.getItem('list')));
  } else {
    return [];
  }
};
function App() {
  const [name, setName] = useState('');
  const [price, setPrice] = useState('');
  const [list, setList] = useState(getLocalStorage());
  const [isEditing, setIsEditing] = useState(false);
  const [editID, setEditID] = useState(null);
  const [alert, setAlert] = useState({ show: false, msg: '', type: '' });
  const handleSubmit = (e) => {
    e.preventDefault();
    if (!name || !price) {
      showAlert(true, 'danger', 'please enter value');
    } else if (name && price && isEditing) {
      setList(
          list.map((item) => {
            if (item.id === editID) {
              return { ...item, title: name, price: price };
            }
            return item;
          })
      );
      setName('');
      setPrice('');
      setEditID(null);
      setIsEditing(false);
      showAlert(true, 'success', 'value changed');
    } else {
      showAlert(true, 'success', 'item added to the list');
      const newItem = { id: new Date().getTime().toString(), title: name,price: price };

      setList([...list, newItem]);
      setName('');
      setPrice('');
    }
  };

  const showAlert = (show = false, type = '', msg = '') => {
    setAlert({ show, type, msg });
  };
  const clearList = () => {
    showAlert(true, 'danger', 'empty list');
    setList([]);
  };
  const removeItem = (id) => {
    showAlert(true, 'danger', 'item removed');
    setList(list.filter((item) => item.id !== id));
  };
  const editItem = (id) => {
    const specificItem = list.find((item) => item.id === id);
    setIsEditing(true);
    setEditID(id);
    setName(specificItem.title);
  };
  useEffect(() => {
    localStorage.setItem('list', JSON.stringify(list));
  }, [list]);
  return (
      <section className='section-center'>
        <form className='grocery-form' onSubmit={handleSubmit}>
          {alert.show && <Alert {...alert} removeAlert={showAlert} list={list} />}

          <h3>Grocery list</h3>
          <div className='form-control'>
            <input
                type='text'
                className='grocery'
                placeholder='item'
                value={name}
                onChange={(e) => setName(e.target.value)}
            />
            <input
              type='text'
              className='grocery'
              placeholder='price'
              value={price}
              onChange={(e) => setPrice(e.target.value)}
          />
            <button type='submit' className='submit-btn'>
              {isEditing ? 'edit' : 'submit'}
            </button>
          </div>
        </form>
        {list.length > 0 && (
            <div className='grocery-container'>
              <List items={list} removeItem={removeItem} editItem={editItem} />
              <button className='calculate-btn' onClick={''}>
                calculate
              </button>
              <button className='clear-btn' onClick={clearList}>
                clear items
              </button>
            </div>
        )}
      </section>
  );
}

export default App;