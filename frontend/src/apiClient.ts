import axios from "axios";

export const fetchBinaryCode = async (
  code: string,
  type: string
): Promise<string> => {
  const url = `/barcode/${type}`;
  const response = await axios.post(url, code, {
    headers: { Accept: "text/plain", "Content-Type": "text/plain" },
  });
  return await response.data;
};

export const fetchBarCode = async (
  code: string,
  type: string
): Promise<string> => {
  const url = `/barcode/${type}`;
  const response = await axios.post(url, code, {
    headers: { Accept: "image/svg+xml", "Content-Type": "text/plain" },
  });
  return await response.data;
};

export const fetchBarCodeList = async (): Promise<string[]> => {
  const response = await axios.get("/barcodes", {});
  return await response.data;
};
