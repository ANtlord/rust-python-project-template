use pyo3::prelude::PyResult;
use pyo3::prelude::PyErr;
use pyo3::prelude::PyModule;
use pyo3::prelude::pyfunction;
use pyo3::prelude::pymodule;
use pyo3::prelude::Python;
use pyo3::wrap_pyfunction;
use pyo3::exceptions;

#[pyfunction]
fn hello() -> PyResult<String> {
    Err(PyErr::new::<exceptions::TypeError, _>("Error message"))
}

#[pymodule]
fn nathello(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(hello))?;
    Ok(())
}
