import { useEffect, useState } from "react";
import { Barcode } from "./Barcode";
import { fetchBarCodeList } from "./apiClient";

function App() {
  const [data, setData] = useState("");
  const [type, setType] = useState("ean8");
  const [typeList, setTypeList] = useState<string[]>([]);
  useEffect(() => {
    (async () => {
      const types = await fetchBarCodeList();
      setTypeList(types);
    })();
  }, []);
  return (
    <div className="App">
      <h1>Barcode</h1>
      <textarea value={data} onChange={(e) => setData(e.target.value)} />
      <select
        value={type}
        onChange={(e) => {
          setType(e.target.value);
        }}
      >
        {typeList.map((barcode) => (
          <option key={barcode}>{barcode}</option>
        ))}
      </select>
      <Barcode type={type} code={data} />
    </div>
  );
}

export default App;
