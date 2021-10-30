import { Barcode } from './Barcode';

function App() {
  return (
    <div className="App">
      <h1>Barcode</h1>
      <Barcode type="ean8" code="1311411"/>
      <Barcode type="ean13" code="978115588507"/>
    </div>
  );
}

export default App;
