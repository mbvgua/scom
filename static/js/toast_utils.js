// Error message extraction from API responses
export function getErrorMessage(error) {
  if (typeof error.detail === "string") {
    return error.detail;
  } else if (Array.isArray(error.detail)) {
    return error.detail.map((err) => err.msg).join(". ");
  }
  return "An error occurred. Please try again.";
}

// show bootstrap toast by ID
export function showToast(toastId) {
  const toast = bootstrap.Toast.getOrCreateInstance(
    document.getElementById(toastId),
  );
  toast.show();
  return toast;
}

// hide bootstrap toast ID
export function hideToast(toastId) {
  const toast = bootstrap.Toast.getInstance(document.getElementById(toastId));
  if (toast) toast.hide();
}
