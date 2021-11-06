import { useCallback, useEffect, useState } from "react";
import { fetchBarCode, fetchBinaryCode } from "./apiClient";
interface Props {
  type: string;
  code: string;
}

export const Barcode = ({ type, code }: Props) => {
  const [binary, setBinary] = useState<string>();
  const [barcode, setBarcode] = useState<string>();
  const [error, setError] = useState(false);

  const update = useCallback(async () => {
    setError(false);
    try {
      const bin = await fetchBinaryCode(code, type);
      setBinary(bin);
      const barcode = await fetchBarCode(code, type);
      setBarcode(barcode);
    } catch (e) {
      setError(true);
    }
  }, [type, code]);

  useEffect(() => {
    update();
  }, [type, code, update]);
  if (error) {
    return <div>ERROR</div>;
  }
  return (
    <table>
      <tbody>
        <tr>
          <th>type</th>
          <td>{type}</td>
        </tr>
        <tr>
          <th>code</th>
          <td>{code}</td>
        </tr>
        <tr>
          <th>binary</th>
          <td>{binary}</td>
        </tr>
        <tr>
          <th>barcode</th>
          <td
            className="content"
            dangerouslySetInnerHTML={{ __html: barcode ?? "" }}
          ></td>
        </tr>
      </tbody>
    </table>
  );
};
