import { useEffect, useState } from "react";

interface Props {
  type: string;
  code: string;
}

export const Barcode = ({ type, code }: Props) => {
  const [binary, setBinary] = useState<string>();
  const [barcode, setBarcode] = useState<string>();

  const update = async () => {
    const bin = await fetchBinaryCode(code);
    setBinary(bin);

    const barcode = await fetchBarCode(code);
    setBarcode(barcode);
  };

  useEffect(() => {
    update();
  });

  return (
    <table>
      <tr>
        <th>type</th> <td>{type}</td>
      </tr>
      <tr>
        <th>code</th> <td>{code}</td>
      </tr>

      <tr>
        <th>binary</th> <td>{binary}</td>
      </tr>
      <tr>
        <th>barcode</th>
        <td
          className="content"
          dangerouslySetInnerHTML={{ __html: barcode ?? "" }}
        ></td>
      </tr>
    </table>
  );
};

const fetchBinaryCode = async (code: string) => {
  const response = await fetch(`/barcode8/${code}`);
  return await response.text();
};

const fetchBarCode = async (code: string) => {
  const response = await fetch(`/bc8_svg/${code}`);
  return await response.text();
};
