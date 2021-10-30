import axios from "axios";

axios.defaults.headers.get = {
  Accept: "application/json",
};

export const fetchBinaryCode = async (
  code: string,
  type: string
): Promise<string> => {
  const url = type === "ean8" ? "barcode8" : "barcode13";
  const response = await axios.get(
    `/${url}/${code}`,
    { headers: { Accept: "text/plain" } }
  );
  return await response.data;
};

export const fetchBarCode = async (
  code: string,
  type: string
): Promise<string> => {
  const url = type === "ean8" ? "bc8_svg" : "bc13_svg";
  const response = await axios.get(`/${url}/${code}`, {
    headers: { Accept: "image/svg+xml" },
  });
  return await response.data;
};
