PROCESS_ENGINEERING_TOPICS = {
    "mass balances": """
Mass balances track material entering, leaving, accumulating, or reacting in a system.
General form: Input - Output + Generation - Consumption = Accumulation.
Common applications include tanks, reactors, separators, recycle loops, and production lines.
""",
    "energy balances": """
Energy balances track heat, work, enthalpy, kinetic energy, potential energy, and accumulation.
They are used in heat exchangers, reactors, evaporators, boilers, and utility systems.
""",
    "fluid flow": """
Fluid flow covers pressure drop, pipe sizing, pumps, valves, flow regimes, and friction losses.
Important concepts include Reynolds number, Bernoulli's equation, pump curves, and system curves.
""",
    "heat transfer": """
Heat transfer includes conduction, convection, and radiation.
Industrial applications include heat exchangers, cooling systems, condensers, evaporators, and furnaces.
""",
    "distillation": """
Distillation separates components based on volatility differences.
Important concepts include vapor-liquid equilibrium, reflux ratio, stages, McCabe-Thiele analysis, and column efficiency.
""",
    "process control": """
Process control maintains variables such as temperature, pressure, level, and flow near desired setpoints.
Key concepts include sensors, controllers, final control elements, PID tuning, disturbances, and stability.
""",
    "process safety": """
Process safety focuses on preventing fires, explosions, toxic releases, overpressure events, and unsafe operating conditions.
Key tools include HAZOP, LOPA, relief design, alarms, interlocks, and management of change.
""",
    "industrial data analysis": """
Industrial data analysis uses process, production, maintenance, quality, and energy data to improve operations.
Applications include dashboards, anomaly detection, forecasting, and root cause analysis.
""",
    "optimization": """
Process optimization improves performance by adjusting variables while respecting constraints.
Examples include reducing energy use, increasing yield, minimizing downtime, and improving throughput.
""",
}


def get_topic_context(topic: str) -> str:
    topic_lower = topic.lower()

    matches = [
        content.strip()
        for key, content in PROCESS_ENGINEERING_TOPICS.items()
        if key in topic_lower
    ]

    if matches:
        return "\n\n".join(matches)

    return """
Relevant process engineering areas include mass balances, energy balances, fluid flow,
heat transfer, process control, process safety, industrial data analysis, and optimization.
"""
