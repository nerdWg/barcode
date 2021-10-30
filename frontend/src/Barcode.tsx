import { useCallback, useEffect, useState } from "react";
type BarcodeType = "ean8" | "ean13";
interface Props {
  type: BarcodeType;
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

const fetchBinaryCode = async (code: string, type: BarcodeType) => {
  const url = type === "ean8" ? "barcode8" : "barcode13";
  const response = await fetch(`/${url}/${code}`);
  return await response.text();
};

const fetchBarCode = async (code: string, type: BarcodeType) => {
  const url = type === "ean8" ? "bc8_svg" : "bc13_svg";
  const response = await fetch(`/${url}/${code}`);
  return await response.text();
};
