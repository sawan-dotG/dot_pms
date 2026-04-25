<template>
  <div class="space-y-6">
    <div class="flex items-center justify-between">
      <div>
        <h2 class="text-3xl font-bold text-white tracking-tight">Objectives & Key Results</h2>
        <p class="text-slate-400 mt-1">Align your goals with the company's vision</p>
      </div>
      <button class="bg-indigo-500 hover:bg-indigo-600 text-white px-5 py-2.5 rounded-xl font-medium transition-colors shadow-lg shadow-indigo-500/30 flex items-center gap-2">
        <i data-feather="plus" class="w-4 h-4"></i> New Objective
      </button>
    </div>

    <!-- OKR Tree View -->
    <div class="glass-card p-6 space-y-6">
      
      <div v-if="objectives.loading" class="text-slate-400">Loading Objectives...</div>
      <div v-else-if="objectives.error" class="bg-red-500/20 text-red-300 p-4 rounded border border-red-500/30">
        Error loading objectives: {{ objectives.error }}
      </div>
      <div v-else-if="!objectives.data || objectives.data.length === 0" class="text-slate-400">No Objectives found. Create one to get started!</div>

      <!-- Objective Item -->
      <div v-else v-for="obj in objectives.data" :key="obj.name" class="bg-slate-800/50 rounded-xl p-5 border border-white/5">
        <div class="flex items-start justify-between">
          <div class="flex-1">
            <div class="flex items-center gap-3 mb-2">
              <span class="px-2.5 py-1 rounded-full bg-indigo-500/20 text-indigo-300 text-xs font-semibold">Objective</span>
              <span class="text-slate-400 text-sm"><i data-feather="users" class="w-4 h-4 inline mr-1"></i> Public</span>
            </div>
            <h3 class="text-xl font-semibold text-white">{{ obj.title }}</h3>
            <p class="text-slate-400 text-sm mt-1">Owner: {{ obj.owner }}</p>
          </div>
          <div class="text-right">
            <div class="text-2xl font-bold text-gradient">{{ Math.round(obj.progress || 0) }}%</div>
            <p class="text-xs text-slate-400">Overall Progress</p>
          </div>
        </div>

        <!-- Key Results -->
        <div class="mt-6 space-y-3">
          
          <div v-if="getKRsForObjective(obj.name).length === 0" class="text-sm text-slate-500 italic">
            No Key Results attached to this Objective.
          </div>

          <div v-for="kr in getKRsForObjective(obj.name)" :key="kr.name" class="glass rounded-lg p-4 flex items-center justify-between group">
            <div class="flex items-center gap-4 flex-1">
              <div class="w-2 h-2 rounded-full" :class="getDotColor(kr.progress)"></div>
              <div class="flex-1">
                <p class="font-medium text-slate-200">{{ kr.title }}</p>
                <div class="w-full bg-slate-700/50 h-1.5 rounded-full mt-2 overflow-hidden">
                  <div class="h-full rounded-full bg-gradient-to-r" :class="getProgressColor(kr.progress)" :style="`width: ${kr.progress || 0}%`"></div>
                </div>
              </div>
            </div>
            <div class="ml-6 text-right">
              <p class="text-sm font-semibold text-white" v-if="kr.target_value">{{ kr.current_value || 0 }} / {{ kr.target_value }}</p>
              <p class="text-sm font-semibold text-white" v-else>{{ Math.round(kr.progress || 0) }}%</p>
              <button class="text-xs text-indigo-400 opacity-0 group-hover:opacity-100 transition-opacity">Update Check-in</button>
            </div>
          </div>

        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { onMounted, computed } from 'vue';
import { createListResource } from 'frappe-ui';
import feather from 'feather-icons';

const objectives = createListResource({
  doctype: 'PMS Objective',
  fields: ['name', 'title', 'owner', 'progress'],
  auto: true
});

const keyResults = createListResource({
  doctype: 'PMS Key Result',
  fields: ['name', 'title', 'objective', 'current_value', 'target_value', 'progress'],
  auto: true
});

const getKRsForObjective = (objectiveName) => {
  if (!keyResults.data) return [];
  return keyResults.data.filter(kr => kr.objective === objectiveName);
};

const getProgressColor = (progress) => {
  if (progress >= 80) return 'from-green-400 to-emerald-400';
  if (progress >= 40) return 'from-amber-400 to-orange-400';
  return 'from-red-400 to-rose-400';
};

const getDotColor = (progress) => {
  if (progress >= 80) return 'bg-green-400';
  if (progress >= 40) return 'bg-amber-400';
  return 'bg-red-400';
};

onMounted(() => {
  feather.replace();
});
</script>
