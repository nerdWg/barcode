import { useState } from "react";
import { Barcode } from "./Barcode";

function App() {
  const [data, setData] = useState("");
  const [type, setType] = useState("ean8");
  return (
    <div className="App">
      <h1>Barcode</h1>
      <input value={data} onChange={(e) => setData(e.target.value)} />
      <select
        value={type}
        onChange={(e) => {
          setType(e.target.value);
        }}
      >
        <option>ean8</option>
        <option>ean13</option>
      </select>
      <Barcode type={type} code={data} />
    </div>
  );
}

export default App;
