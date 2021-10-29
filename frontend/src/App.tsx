import React from 'react';
import './App.css';
import { Barcode } from './Barcode';

function App() {
  return (
    <div className="App">
      <h1>Barcode</h1>
      <Barcode type="ean8" code="00000000"/>
    
    
    </div>
  );
}

export default App;
