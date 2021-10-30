import { useCallback, useEffect, useState } from "react";
import { fetchBarCode, fetchBinaryCode } from "./apiClient";
interface Props {
  type: string;
  code: string;
}

export const Barcode = ({ type, code }: Props) => {
  const [binary, setBinary] = useState<string>();
  const [barcode, setBarcode] = useState<string>();

  const update = useCallback(async () => {
    const bin = await fetchBinaryCode(code, type);
    setBinary(bin);

    const barcode = await fetchBarCode(code, type);
    setBarcode(barcode);
  }, [type, code]);

  useEffect(() => {
    update();
  }, [type, code, update]);

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

